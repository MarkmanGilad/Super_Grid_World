import pygame
from .Constants import *
import numpy as np

FPS = 60
SQUARE_SIZE = 80
LINE_WIDTH = 2
PADDING = 2
FRAME = 2

class Graphics:
    def __init__(self, env) -> None:
        self.env = env
        self.init_screen()
        self.load_robot()
        # self.end_state = self.env.end_state
        np.set_printoptions(linewidth=200)

    def init_screen (self):
        self.rows = self.env.rows
        self.cols = self.env.cols
        
        self.height = self.env.rows * SQUARE_SIZE
        self.width = self.env.cols * SQUARE_SIZE
        
        self.display = pygame.display.set_mode((self.width, self.height + 100))
        self.header = pygame.Surface((self.width, 100))
        self.screen = pygame.Surface((self.width, self.height + 100))
        
        self.display.blit(self.header, (0,0))
        self.display.blit(self.screen, (0,100))
        pygame.display.set_caption('Maze')
        
    
    def load_robot(self):
        robot = pygame.image.load('Img/Robot_1.png')
        self.robot = pygame.transform.scale(robot, (SQUARE_SIZE-20 ,SQUARE_SIZE-20))

    def draw (self, state):
        self.screen.fill(LIGHTGRAY)
        self.header.fill(BLUE)
        self.write(f"Reward: {self.env.reward:.2f}   |   Sum Reward: {self.env.sum_reward:.2f}", 
               pos=(30, 10), color=WHITE, background=BLUE)
        self.write(f"State: {state}    |    Terminal Value: {self.env.board[state]}", 
               pos=(30, 40), color=WHITE, background=BLUE)
        self.draw_lines()
        self.draw_end_state(state)
        self.draw_img(state,self.robot)
        
        self.display.blit(self.header, (0,0))
        self.display.blit(self.screen, (0,100))
        pygame.display.update()
        
    def draw_lines(self):
        for i in range(self.rows+1):
            pygame.draw.line(self.screen, BLACK, (0, i * SQUARE_SIZE), 
                             (self.width, i * SQUARE_SIZE ), width=LINE_WIDTH)
        for i in range(self.cols+1):
            pygame.draw.line(self.screen, BLACK, (i * SQUARE_SIZE, 0), 
                             (i * SQUARE_SIZE , self.height), width=LINE_WIDTH)
    
    def draw_end_state(self, state):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.env.hidden and (row,col) != state:
                    continue
                if self.env.board[row,col] < 0:
                    self.draw_square((row,col), RED)
                    self.draw_txt((row,col),str(self.format_number(self.env.board[row,col])))
                elif self.env.board[row,col] > 0:
                    self.draw_square((row,col), GREEN)
                    self.draw_txt((row,col),str(self.format_number(self.env.board[row,col])))
                else:
                    self.draw_square((row,col), WHITE)
                    

    def draw_square (self, row_col, color):
        pos = self.calc_pos(row_col)
        pygame.draw.rect(self.screen, color, (*pos, SQUARE_SIZE-PADDING, SQUARE_SIZE-PADDING))

    def draw_txt (self, row_col, txt):
        x, y = self.calc_pos(row_col)
        font = pygame.font.SysFont('Ariel', 48)
        txt_surf = font.render(txt, True, BLACK)
        self.screen.blit(txt_surf, (x + 15,y+20))

    def write (self, text, pos = (50, 20), color = BLACK, background=BLUE, font_size = 20):
        surface = self.header
        font = pygame.font.SysFont("arial", font_size)
        text_surface = font.render(text, True, color, background)
        surface.blit(text_surface, pos)
        # self.display.blit(surface, (0,0))
        # pygame.display.update()

    def draw_img (self, row_col, img):
        x, y = self.calc_pos(row_col)
        pos = x + 10, y + 10
        self.screen.blit(img, pos)

    def calc_pos(self, row_col):
        row, col = row_col
        y = row * SQUARE_SIZE + FRAME
        x = col * SQUARE_SIZE + FRAME
        return x, y

    def format_number(self,x):
        return str(int(x)) if x == int(x) else str(x)   

    def __call__(self, state = (0,0)):
        self.draw (state)