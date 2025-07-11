from Code.Environement import Environement
from Code.Agent import *
from Code.Human_Agent import Human_Agent

def main ():

    board = [
        [ 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [-1,-1,-1, 0,-1,-1,-1, 0,-1,-1],
        [ 0, 0, 0, 0,-1, 0,-1, 0,-1, 0],
        [ 0,-1,-1,-1,-1, 0,-1, 0,-1, 0],
        [ 0,-1, 0, 0, 0, 0,-1, 0, 0, 1],
        [ 0, 0, 0,-1,-1, 0, 0,-1,-1,-1],
        [-1,-1,-1,-1, 0, 0,-1, 10, 0, 0],
        [ 0, 0, 0, 0, 0,-1,-1,-1,-1, 0],
        [-1, 0,-1,-1,-1, 0, 0, 0, 0.1, 0],
        [ 0, 0, 0, 0, 0, 0,-1, 0, 0, 0],
    ] 
    start_state = 4,8 #2, 9 
    
    env = Environement(state=start_state, board=board, hidden=True)  
    agent = Human_Agent(env)
    env.agent = agent
    env.delay = 1000
    
    env.play()


if __name__ == '__main__':
    main()


