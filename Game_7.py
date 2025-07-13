from Code.Environement import Environement
from Code.Agent import *
from Code.Human_Agent import Human_Agent
from Code.Constants import *

def main ():

    board = [
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [-1,-1,-1, 0,-1,-1,-1, 0,-1,-1],
        [ 0, 0, 0, 0,-1, 0,-1, 0,-1, 0],
        [ 0,-1,-1,-1,-1, 0,-1, 0,-1, 0],
        [ 0,-1, 0, 0, 0, 0,-1, 0, 0, 0],
        [ 0, 0, 0,-1,-1, 0, 0,-1,-1,-1],
        [-1,-1,-1,-1, 0, 0,-1, 10, 0, 0],
        [ 0, 0, 0, 0, 0,-1,-1,-1,-1, 0],
        [-1, 0,-1,-1,-1, 0, 0, 0, 0, 0],
        [ 0, 0, 0, 0, 0, 0,-1, 0, 0, 0],
    ] 
    start_state = 4,8
      
    env = Environement(state=start_state, board=board, hidden=False)  
    env.step_reward = -0.01
    agent = AI_Agent(env, mode="Value")
    env.agent = agent

    env.reset_delay = 0
    env.delay = 0
    env.train(epochs=200, epsilon=0.01)
    print(env.agent.Value)

    env.reset_delay = 1000
    env.delay = 100
    env.hidden = False
    env.play()

if __name__ == '__main__':
    main()


