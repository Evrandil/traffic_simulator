import random
from simple_traffic_engine import ToyTrafficEnv 

if __name__ == "__main__":
    env = ToyTrafficEnv()
    
    # Rozgrywamy 1 krótki epizod
    state = env.reset()
    print(f"Start symulacji. Stan początkowy: Qa={state[0]}, Qb={state[1]}\n")
    
    total_reward = 0
    
    for step_num in range(1, 101): # Symulujemy 30 sekund/kroków
        # W prawdziwym kodzie ML, tutaj modele wybierałyby akcje na podstawie stanu:
        # action_a = model_A.predict(state)
        # action_b = model_B.predict(state)
        
        # Na razie udajemy, że podejmują losowe decyzje (0 lub 1)
        action_a = random.choice([0, 1])
        action_b = random.choice([0, 1])
        
        # Wysyłamy akcje do środowiska i odbieramy konsekwencje
        next_state, reward, done = env.step(action_a, action_b)
        
        # Tu w przyszłości dodasz: model_A.learn(...) i model_B.learn(...)
        
        print(f"Krok {step_num}: Akcje(A={action_a}, B={action_b}) | Stan po(Qa={next_state[0]}, Qb={next_state[1]}) | Nagroda: {reward}")
        
        total_reward += reward
        state = next_state
        
        if done:
            print("\n🚨 KATASTROFA! Korek w węźle A osiągnął limit. Przerwano symulację.")
            break
            
    print(f"\nKoniec epizodu. Całkowita kara: {total_reward}")
