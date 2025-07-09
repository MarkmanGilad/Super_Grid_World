from Code.Environement import Environement
from Code.Constants import *
from Code.Agent import *



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
    env = Environement(state=start_state, board=board)  
    
    env.agent = AI_Agent(env, mode="Value")
    env.agent.train()
    
    print ('Value*: \n', env.agent.Value)
    # env.agent.Policy_improv()
    print ('Policy*: \n', env.agent.Policy)
    env.play()



if __name__ == '__main__':
    main()
