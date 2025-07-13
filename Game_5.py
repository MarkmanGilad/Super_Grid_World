from Code.Environement import Environement
from Code.Agent import *
from Code.Human_Agent import Human_Agent
from Code.Constants import *

def main ():
    board = secret_board_1
    start_state = 1,2  
    
    env = Environement(state=start_state, board=board, hidden=True)  
    env.agent = AI_Agent(env, mode="Value")
    env.delay, env.reset_delay = 50, 100

    env.train(epochs=5)
    
    print(env.agent.Value)

    env.delay, env.reset_delay = 100, 1000
    env.hidden = False
    env.play()

if __name__ == '__main__':
    main()


