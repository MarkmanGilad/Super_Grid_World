from Code.Environement import Environement
from Code.Agent import *


def main ():

    start_state = 0,0 
    
    env = Environement(state=start_state)  
            
    policy = [
        [3, 3, 3, 3],
        [3, 3, 3, 3],
        [3, 3, 3, 3],
        [3, 3, 3, 3]
        ]
    env.agent.set_policy(policy) 
    
    env.play()


if __name__ == '__main__':
    main()


