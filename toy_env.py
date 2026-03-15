# toy_env.py
import random

class ToyTrafficEnv:
    def __init__(self):
        self.q_a = 0  
        self.q_b = 0  
        self.max_capacity_b = 5  
        self.max_queue_a = 20    

    def reset(self):
        self.q_a = 0
        self.q_b = 0
        return (self.q_a, self.q_b)

    def step(self, action_a, action_b):
        if action_b == 1 and self.q_b > 0:
            self.q_b -= 1

        if action_a == 1 and self.q_a > 0:
            if self.q_b < self.max_capacity_b:
                self.q_a -= 1
                self.q_b += 1

        if random.random() < 0.5:
            self.q_a += 1

        reward = -(self.q_a + self.q_b)
        done = self.q_a >= self.max_queue_a

        return (self.q_a, self.q_b), reward, done
