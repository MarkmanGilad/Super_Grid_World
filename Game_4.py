from Code.Environement import Environement
from Code.Agent import *
from Code.Human_Agent import Human_Agent
from Code.Constants import *

def main ():

    board = secret_board_1
    # board = secret_board_2
   
    start_state = 1,2  
    
    env = Environement(state=start_state, board=board, hidden=False)  
    agent = Human_Agent(env)
    env.agent = agent
        
    env.play()


if __name__ == '__main__':
    main()


