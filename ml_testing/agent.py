# agent.py
import torch
import torch.nn as nn
import torch.optim as optim
import random
from collections import deque

# 1. Definicja Architektury Sieci Neuronowej
class QNetwork(nn.Module):
    def __init__(self, state_size, action_size):
        super(QNetwork, self).__init__()
        # Bardzo prosta sieć: 2 wejścia -> 16 neuronów -> 2 wyjścia
        self.fc1 = nn.Linear(state_size, 16)
        self.relu = nn.ReLU()
        self.fc2 = nn.Linear(16, action_size)

    def forward(self, state):
        x = self.relu(self.fc1(state))
        return self.fc2(x) # Zwraca Q-values dla obu akcji

# 2. Definicja Agenta
class DQNAgent:
    def __init__(self, state_size, action_size, learning_rate=0.001):
        self.state_size = state_size
        self.action_size = action_size
        
        # Inicjalizacja sieci i optymalizatora
        self.model = QNetwork(state_size, action_size)
        self.optimizer = optim.Adam(self.model.parameters(), lr=learning_rate)
        self.criterion = nn.MSELoss() # Błąd średniokwadratowy
        
        # Pamięć i hiperparametry
        self.memory = deque(maxlen=2000) # Pamięta 2000 ostatnich kroków
        self.gamma = 0.95    # Współczynnik dyskontowania (jak bardzo zależy mu na przyszłości)
        self.epsilon = 1.0   # Eksploracja (na początku 100% losowych akcji)
        self.epsilon_min = 0.05
        self.epsilon_decay = 0.997

    def act(self, state):
        # Strategia Epsilon-Greedy: czasem eksplorujemy (losowo), czasem eksploatujemy (sieć)
        if random.random() <= self.epsilon:
            return random.randrange(self.action_size)
            
        # Jeśli nie losowo, pytamy sieć neuronową o zdanie
        state_tensor = torch.FloatTensor(state).unsqueeze(0) # Zmiana na tensor PyTorcha
        with torch.no_grad():
            q_values = self.model(state_tensor)
        return torch.argmax(q_values).item() # Wybierz akcję z najwyższym Q-value

    def remember(self, state, action, reward, next_state, done):
        # Zapisz doświadczenie do pamięci
        self.memory.append((state, action, reward, next_state, done))

    def replay(self, batch_size):
        # Agent uczy się tylko, gdy ma wystarczająco dużo wspomnień
        if len(self.memory) < batch_size:
            return

        # Pobierz losową "paczkę" wspomnień z bufora
        minibatch = random.sample(self.memory, batch_size)
        
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                # Równanie Bellmana: Przewidujemy przyszłą nagrodę
                next_state_tensor = torch.FloatTensor(next_state).unsqueeze(0)
                future_q = torch.max(self.model(next_state_tensor)).item()
                target = reward + self.gamma * future_q
                
            state_tensor = torch.FloatTensor(state).unsqueeze(0)
            current_q_values = self.model(state_tensor)
            
            # Tworzymy "oczekiwane" wartości Q, podmieniając tylko tę dla wykonanej akcji
            target_q_values = current_q_values.clone()
            target_q_values[0][action] = target
            
            # Obliczamy błąd i aktualizujemy wagi sieci (Backpropagation)
            loss = self.criterion(current_q_values, target_q_values)
            self.optimizer.zero_grad()
            loss.backward()
            self.optimizer.step()

    def decay_epsilon(self):
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay
