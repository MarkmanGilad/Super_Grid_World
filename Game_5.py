from Code.Environement import Environement
from Code.Agent import *
from Code.Human_Agent import Human_Agent
from Code.Constants import *

def main ():

    board = secret_board
   
    start_state = 0,3  
    
    env = Environement(state=start_state, board=board, hidden=True)  
    agent = AI_Agent(env, mode="Q_Table")
    env.agent = agent
    env.reset_delay = 10
    env.delay = 0
    env.train(epochs=500, epsilon=0.9)
    print(env.agent.Q_table)

    env.reset_delay = 1000
    env.delay = 100
    env.hidden = False
    env.play()

if __name__ == '__main__':
    main()


