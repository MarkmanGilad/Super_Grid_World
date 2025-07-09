import pygame
from Graphics import *
from Environement import Environement
from Agent import *

pygame.init()
clock = pygame.time.Clock()
env = Environement((0,0))
graphics = Graphics(env)
# agent = Random_Agent(env)
agent = AI_Agent(env)
# print ('Policy: \n ',agent.Policy)
# print ('Value \n', agent.Value)
# agent.policy_eval()
# print ('Value: \n', agent.Value)
# print(agent.Policy_improv())
# print ('Policy: \n', agent.Policy)
print(agent.Policy_Iteration())
print ('Value*: \n', agent.Value)
print ('Policy*: \n', agent.Policy)
# agent.Value_iteration()
# print ('Value*: \n', agent.Value)
# print ('Policy*: \n', agent.Policy)


def main ():
    run = True
    while (run):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
               run = False
        
        action = agent(env.state)
        pygame.time.wait(100)
        env.state, reward = env.move(env.state, action)
        agent.add_reward(reward)
        graphics(env.state)
        print (f'{agent.Reward} ', end='\r')
        if env.end_of_game(env.state):
            pygame.time.wait(500)
            env.reset()
            graphics(env.state)
        clock.tick(FPS)
    
    pygame.time.wait(200)



if __name__ == '__main__':
    main()
