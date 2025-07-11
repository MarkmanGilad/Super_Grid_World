from Code.Environement import Environement
from Code.Agent import *


def main ():

    start_state = 0,3 
    board = [
        [0, 0, 0, 0],
        [0, -1, -1, -1],
        [0, 0, 0, 0],
        [0, -1, 0, 1],
        ]
    
    value = [
        [0.4, 0.3, 0.2, 0.1],
        [0.5, 0. , 0. , 0. ],
        [0.6, 0.7, 0.8, 0.9],
        [0.5, 0. , 0.9, 0. ]]

    env = Environement(state=start_state, board=board)  

    env.agent.set_value(value)   

    env.agent.mode = "Value"   
    
    env.play()


if __name__ == '__main__':
    main()


