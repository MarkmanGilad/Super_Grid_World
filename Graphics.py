import pygame


FPS = 60
ROWS, COLS = 5, 5 #5,5   
SQUARE_SIZE = 80
LINE_WIDTH = 2
PADDING = 2
HEIGHT, WIDTH  = ROWS * (SQUARE_SIZE), COLS * (SQUARE_SIZE)
FRAME = 2



#RGB
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
LIGHTGRAY = (211,211,211)
GREEN = (0, 128, 0)

class Graphics:
    def __init__(self, env) -> None:
        self.env = env
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Maze')
        self.load_img()

    def load_img(self):
        robot = pygame.image.load('Img/Robot_1.png')
        self.robot = pygame.transform.scale(robot, (SQUARE_SIZE-20 ,SQUARE_SIZE-20))

    def draw (self, state):
        self.screen.fill(LIGHTGRAY)
        self.draw_lines()
        self.draw_end_squares()
        self.draw_img(state,self.robot)
        pygame.display.update()
        
    def draw_lines(self):
        for i in range(ROWS+1):
            pygame.draw.line(self.screen, BLACK, (0, i * SQUARE_SIZE), 
                             (WIDTH, i * SQUARE_SIZE ), width=LINE_WIDTH)
        for i in range(COLS+1):
            pygame.draw.line(self.screen, BLACK, (i * SQUARE_SIZE, 0), 
                             (i * SQUARE_SIZE , HEIGHT), width=LINE_WIDTH)
    
    def draw_end_squares(self):
        for row in range(ROWS):
            for col in range(COLS):
                if self.env.board[row,col] == -1:
                    self.draw_square((row,col), RED)
                    self.draw_txt((row,col),"-1")
                if self.env.board[row,col] == 1:
                    self.draw_square((row,col), GREEN)
                    self.draw_txt((row,col),"+1")

    def draw_square (self, row_col, color):
        pos = self.calc_pos(row_col)
        pygame.draw.rect(self.screen, color, (*pos, SQUARE_SIZE-PADDING, SQUARE_SIZE-PADDING))

    def draw_txt (self, row_col, txt):
        x, y = self.calc_pos(row_col)
        font = pygame.font.SysFont('Ariel', 48)
        txt_surf = font.render(txt, True, BLACK)
        self.screen.blit(txt_surf, (x + 20,y+20))

    def draw_img (self, row_col, img):
        x, y = self.calc_pos(row_col)
        pos = x + 10, y + 10
        self.screen.blit(img, pos)

    def calc_pos(self, row_col):
        row, col = row_col
        y = row * SQUARE_SIZE + FRAME
        x = col * SQUARE_SIZE + FRAME
        return x, y

    def __call__(self, state = (0,0)):
        self.draw (state)