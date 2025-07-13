from Code.Environement import Environement
from Code.Agent import *


def main ():

    # start_state = 0,0 
    # board = [
    #     [0, 0, 0, 0],
    #     [0, 0, 0, -1],
    #     [0, 0, 0, 0],
    #     [0, 0, 0, 1],
    #     ]
    # board = [
    #     [1, -1, 0, 0],
    #     [0, 0, 0, -1],
    #     [0, 0, 0, 0],
    #     [1, 0, 0, 0],
    #     ]
    # board = [
    #     [0, 0, 0,0, -1, 0,],
    #     [-1, -1, 0, 0,-1, 1],
    #     [1, -1, 0, 0, -1, 0],
    #     [0, 0, 0, 0, 0, 0],
    #     [0, 0, -1, -1, -1, 0],
    #     [0, 0, -1, 1, 0, 0],
    #     ]
    start_state = 0,3 
    board = [
        [0, 0, 0, 0],
        [0, -1, -1, -1],
        [0, 0, 0, 0],
        [0, -1, 0, 1],
        ]
    env = Environement(state=start_state, board=board)  
           
       
    env.agent.value_iteration()
    
    print ('Value*: \n', env.agent.Value)
    env.agent.Policy_from_value()
    print ('Policy*: \n', env.agent.Policy)
    env.play()


if __name__ == '__main__':
    main()


