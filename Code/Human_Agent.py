import pygame as pg
from .Action import Action

class Human_Agent:
    def __init__(self, env):
        self.env = env

    def get_action(self, state):
        for event in self.env.events:  # Access events from environment
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    return Action.LEFT
                elif event.key == pg.K_RIGHT:
                    return Action.RIGHT
                elif event.key == pg.K_UP:
                    return Action.UP
                elif event.key == pg.K_DOWN:
                    return Action.DOWN
        return None
    def __call__(self, state):
        return self.get_action(state)
