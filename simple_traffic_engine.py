import random

class ToyTrafficEnv:
    def __init__(self):
        # Inicjalizacja stanu środowiska
        self.q_a = 0  # Kolejka przed węzłem A
        self.q_b = 0  # Kolejka przed węzłem B
        self.max_capacity_b = 5  # Węzeł B pomieści max 5 aut!
        self.max_queue_a = 20    # Jeśli A urośnie do 20, kończymy symulację (przegrana)

    def reset(self):
        """Zaczynamy nowy epizod z czystą kartą."""
        self.q_a = 0
        self.q_b = 0
        return (self.q_a, self.q_b)

    def step(self, action_a, action_b):
        """
        action_a: 1 (przepuść auto), 0 (czerwone światło)
        action_b: 1 (przepuść auto), 0 (czerwone światło)
        """
        
        # 1. Węzeł B wypuszcza auta z systemu (jeśli ma zielone i są tam auta)
        if action_b == 1 and self.q_b > 0:
            self.q_b -= 1

        # 2. Węzeł A przesyła auta do węzła B
        if action_a == 1 and self.q_a > 0:
            if self.q_b < self.max_capacity_b:
                self.q_a -= 1
                self.q_b += 1
            else:
                # Agent A podjął złą decyzję! Próbuje wepchnąć auto do pełnego węzła B.
                # Auto zostaje w A (tworzy się gridlock/zator).
                pass 

        # 3. Nowe auta dojeżdżają z miasta do węzła A (np. 50% szans w każdej sekundzie)
        if random.random() < 0.5:
            self.q_a += 1

        # 4. Obliczenie WSPÓLNEJ nagrody (Global Shared Reward)
        # Karzemy agentów za każde auto stojące w korku
        reward = -(self.q_a + self.q_b)

        # 5. Sprawdzamy, czy epizod się kończy (korek rozlał się na całe miasto)
        done = self.q_a >= self.max_queue_a

        # Zwracamy nowy stan, nagrodę i flagę końca
        return (self.q_a, self.q_b), reward, done
