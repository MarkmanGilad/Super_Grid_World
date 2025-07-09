from Graphics import *
from Action import Action
import numpy as np

class Environement:
    def __init__(self, state = (0,0)):
        self.state = state
        self.board = np.zeros((ROWS, COLS))
        # self.board[1,2] = -1
        # self.board[3,3] = 1

        self.board[1,0] = -1
        self.board[1,1] = -1
        self.board[1,2] = -1
        self.board[1,4] = -1
        self.board[3,1] = -1
        self.board[3,2] = -1
        self.board[3,3] = -1
        self.board[3,4] = -1
        self.board[4,4] = 1

    def reset(self):
        self.state = (0,0)

    def move (self, state, action: Action):
        row, col = state
        x,y = 0, 0
        if action == Action.UP and row > 0 :
            y = -1
        elif action == Action.DOWN and row < ROWS - 1:
            y = 1
        elif action == Action.LEFT and col > 0:
            x = -1
        elif action == Action.RIGHT and col < COLS -1:
            x = 1
        new_state = row + y, col + x
        reward = self.Reward(new_state)
        return new_state, reward

    def Reward (self, new_state):
        return self.board[new_state]

    def get_actions (self, state):
        actions = []
        row, col = state
        if row > 0 :
           actions.append(Action.UP)
        if row < ROWS - 1:
           actions.append(Action.DOWN)       
        if col > 0:
           actions.append(Action.LEFT)
        if col < COLS -1:
           actions.append(Action.RIGHT)
        return actions

    def end_of_game(self, state):
        if self.board[state] != 0:
            return True
        return False
    
    def __call__(self, state, action):
        return self.move(state, action)
        