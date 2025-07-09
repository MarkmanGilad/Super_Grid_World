from enum import Enum

class Action (Enum):
    UP = 0
    RIGHT = 1
    LEFT = 2
    DOWN = 3

    def inverse (self, action):
        match action:
            case Action.UP: return Action.DOWN
            case Action.DOWN: return Action.UP
            case Action.RIGHT: return Action.LEFT
            case Action.LEFT: return Action.RIGHT

    