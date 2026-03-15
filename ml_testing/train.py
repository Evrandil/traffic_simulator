# train.py
from toy_env import ToyTrafficEnv
from agent import DQNAgent
import matplotlib.pyplot as plt

if __name__ == "__main__":
    env = ToyTrafficEnv()
    
    # Rozmiar stanu to 2 (Qa i Qb), rozmiar akcji to 2 (Przepuść, Czekaj)
    state_size = 2
    action_size = 2
    
    # Tworzymy dwóch niezależnych agentów
    agent_a = DQNAgent(state_size, action_size)
    agent_b = DQNAgent(state_size, action_size)
    
    batch_size = 32
    episodes = 1000 # Trenujemy przez 200 pełnych "gier"
    
    # LISTY NA DANE DO WYKRESÓW
    history_rewards = []
    history_epsilons = []
    
    for e in range(episodes):
        state = env.reset()
        total_reward = 0
        
        for step_num in range(50): # Maksymalnie 50 sekund na epizod
            # Agenci wybierają akcje na podstawie aktualnego stanu
            action_a = agent_a.act(state)
            action_b = agent_b.act(state)
            
            # Wykonujemy krok w środowisku
            next_state, reward, done = env.step(action_a, action_b)
            total_reward += reward
            
            # Obaj agenci ZAPISUJĄ doświadczenie ze WSPÓLNĄ nagrodą
            agent_a.remember(state, action_a, reward, next_state, done)
            agent_b.remember(state, action_b, reward, next_state, done)
            
            state = next_state
            
            if done:
                break
        
        for _ in range(5):
            agent_a.replay(batch_size)
            agent_b.replay(batch_size)       
        
        agent_a.decay_epsilon()
        agent_b.decay_epsilon()

        # ZAPISUJEMY DANE Z TEGO EPIZODU
        history_rewards.append(total_reward)
        history_epsilons.append(agent_a.epsilon)

        # Wypisujemy podsumowanie co kilkanaście epizodów
        print(f"Epizod: {e+1}/{episodes} | Zysk: {total_reward} | Kroków: {step_num} | Epsilon: {agent_a.epsilon:.2f}")
        
    print("Trening zakończony! Generuję wykres...")

    # --- RYSOWANIE WYKRESÓW ---
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

    # Górny wykres: Historia nagród (Krzywa uczenia)
    ax1.plot(history_rewards, color='blue', alpha=0.6, label='Nagroda w epizodzie')
    
    # Dodajemy wygładzoną średnią kroczącą (np. z 10 epizodów), bo wykresy RL mocno skaczą
    window_size = 10
    if len(history_rewards) >= window_size:
        smoothed_rewards = [sum(history_rewards[i:i+window_size])/window_size for i in range(len(history_rewards)-window_size+1)]
        # Przesuwamy oś X dla średniej, żeby pasowała do oryginalnych danych
        ax1.plot(range(window_size-1, len(history_rewards)), smoothed_rewards, color='red', linewidth=2, label='Średnia z 10 epizodów')

    ax1.set_title('Krzywa uczenia Agentów (Nagroda)')
    ax1.set_ylabel('Suma nagród (bliżej zera = lepiej)')
    ax1.legend()
    ax1.grid(True)

    # Dolny wykres: Spadek Epsilona
    ax2.plot(history_epsilons, color='green', linewidth=2)
    ax2.set_title('Spadek parametru Epsilon (Eksploracja -> Eksploatacja)')
    ax2.set_xlabel('Numer Epizodu')
    ax2.set_ylabel('Wartość Epsilon')
    ax2.grid(True)

    plt.tight_layout()
    plt.savefig('learning_curve.png', dpi = 300, bbox_inches = 'tight')
    print('Wykres wygenerowany.')
