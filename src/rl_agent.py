import numpy as np

class QLearningAgent:
    def __init__(self, actions=['Stop', 'Slow', 'Go']):
        self.q_table = {}
        self.actions = actions
        self.lr = 0.1
        self.gamma = 0.9

    def get_reward(self, sign, action):
        # Reward Logic for Ethics/Policy
        if sign == 'Stop' and action == 'Stop': return 10
        if sign == 'Stop' and action == 'Go': return -50
        return 1

print("RL Agent Q-Table initialized. Reward function mapped to safety logic.")
