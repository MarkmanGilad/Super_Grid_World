from .Graphics import *
from .Action import Action
import numpy as np
from .Agent import AI_Agent
import random
import math

class Environement:
    def __init__(self, state = (0,0), board = None, hidden = False, agent = None):
        self.init_state = state
        self.state = state
        self.set_board (board)
        pygame.init()
        self.clock = pygame.time.Clock()
        self.graphics = Graphics(self)
        if agent:
            self.agent = agent
        else:    
            self.agent = AI_Agent(self)
        self.hidden = hidden
        self.reset_delay = 1000
        self.delay = 100
        self.reward = 0
        self.sum_reward = 0
        self.step_reward = -0.1

    def reset(self):
        pygame.time.wait(self.reset_delay)
        self.state = self.init_state
        self.set_board(self.init_board)
        self.sum_reward = 0
        self.reward = 0

    # def set_end_state(self, reward, color):
    #     self.end_state[reward] = color

    def set_board (self, mat=None):
        if mat is not None :
            self.board = np.array(mat)
            self.rows, self.cols = len(mat), len(mat[0])
            self.init_board = self.board.copy()
            return
        
        self.rows, self.cols = 4, 4
        self.board = np.zeros((self.rows, self.cols))
        self.board[1,2] = -1
        self.board[3,3] = 1
        self.init_board = self.board.copy()
        
        # self.board[1,0] = -1
        # self.board[1,1] = -1
        # self.board[1,2] = -1
        # self.board[1,4] = -1
        # self.board[3,1] = -1
        # self.board[3,2] = -1
        # self.board[3,3] = -1
        # self.board[3,4] = -1
        # self.board[4,4] = 1

    def move (self, state, action: Action):
        row, col = state
        x,y = 0, 0
        if action == Action.UP and row > 0 :
            y = -1
        elif action == Action.DOWN and row < self.rows - 1:
            y = 1
        elif action == Action.LEFT and col > 0:
            x = -1
        elif action == Action.RIGHT and col < self.cols -1:
            x = 1
        new_state = row + y, col + x
        reward = self.Reward(new_state, action)
        
        return new_state, reward

    def Reward (self, new_state, action):
        if action is None:
            return 0
        return self.step_reward + float(self.board[new_state])

    def get_actions (self, state):
        actions = []
        row, col = state
        if row > 0 :
           actions.append(Action.UP)
        if row < self.rows - 1:
           actions.append(Action.DOWN)       
        if col > 0:
           actions.append(Action.LEFT)
        if col < self.cols -1:
           actions.append(Action.RIGHT)
        return actions

    def end_of_game(self, state):
        if self.board[state] != 0:
            return True
        return False
        
    def play (self):
        run = True
        self.reset()
        self.graphics(self.state)
        pygame.time.wait(self.reset_delay)
        while (run):
            self.events = pygame.event.get() 
            for event in self.events:
                if event.type == pygame.QUIT:
                    run = False
            
            action = self.agent(self.state) 
            pygame.time.delay(self.delay) 
            self.state, reward = self.move(self.state, action)
            if reward != 0:
                self.reward = reward
                self.sum_reward += self.reward
            self.graphics(self.state)
            if self.end_of_game(self.state):
                self.reset()
                self.graphics(self.state)
            self.clock.tick(FPS)
        
        pygame.time.wait(self.reset_delay)
        pygame.quit()
    
    def train (self, epochs=100, epsilon=0.7, visualize=True, gamma=1.0):
        max_steps = 1
        for epoch in range(epochs):
            self.reset()
            self.graphics(self.state)
            print(epoch, end='\r')
            step = 0
            while not self.end_of_game(self.state):
                step += 1
                self.events = pygame.event.get() 
                for event in self.events:
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return

                if step / max_steps > 0.9:
                    eps = 0.5
                else:
                    eps = 0
                if random.random() < eps:
                    action = random.choice(list(Action))
                else:
                    action = self.agent.get_action(self.state)
                pygame.time.delay(self.delay)
                next_state, reward = self.move(self.state, action)
                if reward != 0:
                    self.reward = reward
                    self.sum_reward += self.reward
                
                state_action = self.state[0], self.state[1], action.value
                next_state_action = next_state[0], next_state[1], self.agent.get_action_from_Q_table(next_state).value

                self.agent.Q_table[state_action] = reward + self.agent.Q_table[next_state_action]
                self.state = next_state
                self.graphics(self.state)
                self.clock.tick(FPS)
            max_steps = max(step, max_steps)
            
        pygame.time.wait(self.reset_delay)
        print("End training...")
        


    def __call__(self, state, action):
        return self.move(state, action)
