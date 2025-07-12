from Code.Environement import Environement
from Code.Agent import *
from Code.Human_Agent import Human_Agent
from Code.Constants import *

def main ():

    board = secret_board
   
    start_state = 1,2  
    
    env = Environement(state=start_state, board=board, hidden=True)  
    agent = AI_Agent(env, mode="Q_Table")
    env.agent = agent
    env.reset_delay = 1000
    
    env.play()


if __name__ == '__main__':
    main()


