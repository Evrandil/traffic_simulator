# train.py
from toy_env import ToyTrafficEnv
from agent import DQNAgent

if __name__ == "__main__":
    env = ToyTrafficEnv()
    
    # Rozmiar stanu to 2 (Qa i Qb), rozmiar akcji to 2 (Przepuść, Czekaj)
    state_size = 2
    action_size = 2
    
    # Tworzymy dwóch niezależnych agentów
    agent_a = DQNAgent(state_size, action_size)
    agent_b = DQNAgent(state_size, action_size)
    
    batch_size = 32
    episodes = 200 # Trenujemy przez 200 pełnych "gier"
    
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
            
            # Obaj agenci się UCZĄ (jeśli mają już dość danych w pamięci)
            agent_a.replay(batch_size)
            agent_b.replay(batch_size)
            
            state = next_state
            
            if done:
                break
                
        # Wypisujemy podsumowanie co kilkanaście epizodów
        print(f"Epizod: {e+1}/{episodes} | Zysk: {total_reward} | Kroków: {step_num} | Epsilon: {agent_a.epsilon:.2f}")
