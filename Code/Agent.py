import numpy as np
from .Action import Action
import math
import pygame

class AI_Agent:
    def __init__(self, env, mode = "policy") -> None:
        self.env = env
        self.Reward = 0
        self.Policy = np.full((self.env.rows, self.env.cols), 3)
        self.Value = np.zeros((self.env.rows, self.env.cols))
        # self.Q_table = np.zeros((self.env.rows, self.env.cols, len(Action)))
        self.mode = mode

    def get_action(self, state):
        if self.mode == "policy":
            return Action(self.Policy[state])
        elif self.mode == "Value":
            action, _ = self.get_best_action_value(state)
            return action
            # return self.get_action_from_Value(state)
        else:
            return NotImplemented
         
    def get_action_from_Value (self, state):
        # return NotImplemented
        # Write your code here
        for action in Action:
            new_state, reward = self.env.move(state, action)
            if np.isclose(self.Value[state], reward + self.Value[new_state]):
                return action
        return None

    def get_best_action_value (self, state):
        steps = [(-1 ,0), (0,1), (0, -1), (1, 0)] # up, right, left, down
        values = []
        for step in steps:
            adj_state = state[0] + step[0], state[1] + step[1]
            if 0 <= adj_state[0] < self.env.rows and 0 <= adj_state[1] < self.env.cols:
                values.append(self.Value[adj_state])
            else:
                values.append(-math.inf)
        values = np.array(values)
        best_idx = np.argmax(values)
        best_action = Action(best_idx)
        best_value = values[best_idx].item()
        return best_action, best_value

    def add_reward(self, reward):
        self.Reward += reward

    def set_policy(self, policy):
        self.Policy = np.array(policy)

    def set_value (self, value):
        self.Value = np.array(value)
    
    def Policy_from_value (self):
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
                    if v_max < reward + self.Value[new_state]:
                        v_max = reward + self.Value[new_state]                            
                        best_action = action
                if self.Policy[state] != best_action.value:
                    self.Policy[state] = best_action.value
                    stable = False
        return stable

    def value_iteration (self, epochs = 100):
        for epoch in range(epochs):
            for row in range(self.env.rows):
                for col in range(self.env.cols):
                    state = row, col
                    if self.env.end_of_game(state):
                        self.Value[state] = self.env.board[state]
                        continue
                    best_value = -math.inf
                    for action in Action:   
                        next_state, reward = self.env(state, action)
                        new_value = reward + self.Value[next_state]
                        if new_value > best_value:
                            best_value = new_value
                    self.Value[state] = best_value

    
    def __call__(self, state):
        return self.get_action(state)
    

    