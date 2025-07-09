import random
import numpy as np
from .Action import Action
import math


class Random_Agent:
    def __init__(self, env) -> None:
        self.env = env
        self.Reward = 0
    
    def get_action(self, state):
        actions = self.env.get_actions(state)
        return random.choice(actions)
            
    def add_reward(self, reward):
        self.Reward += reward

    def __call__(self, state):
        return self.get_action(state)
    
class AI_Agent:
    def __init__(self, env, mode = "policy") -> None:
        self.env = env
        self.Reward = 0
        self.Policy = np.full((self.env.rows, self.env.cols), 3)
        self.Value = np.zeros((self.env.rows, self.env.cols))
        self.gamma = 1
        self.mode = mode


    def get_action(self, state):
        if self.mode == "policy":
            return Action(self.Policy[state])
        else:
            return self.get_action_from_Value(state)
         
    def get_action_from_Value (self, state):
        v_max = -math.inf
        best_action = None
        for action in Action:
            new_state, reward = self.env.move(state, action)
            if v_max < reward + self.gamma * self.Value[new_state]:
                v_max = reward + self.gamma * self.Value[new_state]                            
                best_action = action
        return best_action

    def add_reward(self, reward):
        self.Reward += reward

    def set_policy(self, policy):
        self.Policy = np.array(policy)

    # region
    def policy_eval (self):
        accuracy = 0.0001
        acc = 1
        while acc > accuracy:
            acc = 0
            for row in range(self.env.rows):
                for col in range(self.env.cols):
                    state = row,col
                    if self.env.board[state] != 0:
                        continue
                    old_value = self.Value[state]
                    action = Action(self.Policy[state])
                    new_state, reward = self.env(state, action)
                    new_value = reward + self.gamma * self.Value[new_state]
                    self.Value[state] = new_value
                    acc = max(acc, abs(old_value - new_value))

    def Policy_improv (self):
        stable = True
        for row in range(self.env.rows):
            for col in range(self.env.cols):
                state = row,col
                if self.env.board[state] != 0:
                    continue
                v_max = -math.inf
                best_action = None
                for action in Action:
                    new_state, reward = self.env.move(state, action)
                    if v_max < reward + self.gamma * self.Value[new_state]:
                        v_max = reward + self.gamma * self.Value[new_state]                            
                        best_action = action
                if self.Policy[state] != best_action.value:
                    self.Policy[state] = best_action.value
                    stable = False
        return stable
    

    def Policy_Iteration (self):
        policy_stable = False

        while not policy_stable:
            self.policy_eval()
            policy_stable = self.Policy_improv()
        return policy_stable

    # endregion

    def train (self):
        accuracy = 0.00001
        acc = 1
        # while acc> accuracy:
        for epoch in range(100):
            acc = 0
            for row in range(self.env.rows):
                for col in range(self.env.cols):
                    state = row, col
                    if self.env.end_of_game(state):
                        continue
                    best_value = -1000
                    for action in Action:   # only legal actions
                        new_state, reward = self.env(state, action)
                        new_value = reward + self.gamma * self.Value[new_state]
                        if new_value > best_value:
                            best_value = new_value
                    old_value = self.Value[state]
                    self.Value[state] = best_value
                    acc = max(acc, abs(old_value - best_value))
        
        # self.Policy_improv()

    def __call__(self, state):
        return self.get_action(state)
    

    