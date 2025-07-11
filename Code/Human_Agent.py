import pygame as pg
from .Action import Action

class Human_Agent:
    def __init__(self, env):
        self.env = env

    def get_action(self, state):
        keys = pg.key.get_pressed()
        if not keys:
            return None
                
        if keys[pg.K_LEFT]:
            return Action.LEFT
        elif keys[pg.K_RIGHT]:
            return Action.RIGHT
        elif keys[pg.K_UP]:
            return Action.UP
        elif keys[pg.K_DOWN]:
            return Action.DOWN
        else:
            return None
        
    def __call__(self, state):
        return self.get_action(state)
