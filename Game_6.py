from Code.Environement import Environement
from Code.Agent import *
from Code.Human_Agent import Human_Agent
from Code.Constants import *

def main ():

    board = secret_board_2
   
    start_state = 0,3  
    
    env = Environement(state=start_state, board=board, hidden=False)  
    agent = AI_Agent(env, mode="Value")
    env.agent = agent
    env.reset_delay = 0
    env.delay = 0
    env.train(epochs=300, epsilon=0.0)
    print(agent.Value)
    env.reset_delay = 1000
    env.delay = 100
    env.hidden = False
    env.play()

if __name__ == '__main__':
    main()


