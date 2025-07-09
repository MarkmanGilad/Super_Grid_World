from .Graphics import *
from .Action import Action
import numpy as np
from .Agent import AI_Agent

class Environement:
    def __init__(self, state = (0,0), board = None):
        self.init_state = state
        self.state = state
        self.set_board (board)
        pygame.init()
        self.clock = pygame.time.Clock()
        self.graphics = Graphics(self)

    def reset(self):
        self.state = self.init_state
        self.set_board(self.init_board)

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
        reward = self.Reward(new_state)
        
        return new_state, reward

    def Reward (self, new_state):
        return -0.1 + float(self.board[new_state])

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
        while (run):
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    run = False
            
            action = self.agent(self.state)
            pygame.time.wait(100)
            self.state, reward = self.move(self.state, action)
            self.agent.add_reward(reward)
            self.graphics(self.state)
            # print (f'{agent.Reward} ', end='\r')
            if self.end_of_game(self.state):
                pygame.time.wait(100)
                self.reset()
                self.graphics(self.state)
            self.clock.tick(FPS)
        
        pygame.time.wait(200)
        pygame.quit()

    def __call__(self, state, action):
        return self.move(state, action)
        