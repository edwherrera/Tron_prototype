from Logic.player import Player
from Logic.exception import InvalidActionException

class MoveUp:
    def __init__(self, player, spaces):
        self.player = player
        self.spaces = spaces

    def perform(self):
        self.player.move(vertical=self.spaces)


class MoveDown:
    def __init__(self, player, spaces):
        self.player = player
        self.spaces = spaces

    def perform(self):
        self.player.move(vertical=-self.spaces)


class MoveRight:
    def __init__(self, player, spaces):
        self.player = player
        self.spaces = spaces

    def perform(self):
        self.player.move(horizontal=self.spaces)


class MoveLeft:
    def __init__(self, player, spaces):
        self.player = player
        self.spaces = spaces

    def perform(self):
        self.player.move(horizontal=-self.spaces)


def perform_action(action, board_width, board_height):
    action.perform()
    adjust_position(action.player, board_width, board_height)
    return action.player


def adjust_position(player, board_width, board_height):
    player.position['x'] %= board_width
    player.position['y'] %= board_height


def get_action(name, player, spaces):
    new_action = {
        'up': MoveUp,
        'down': MoveDown,
        'left': MoveLeft,
        'right': MoveRight
    }.get(name)

    if new_action is None:
        raise InvalidActionException(name, "is not a valid action")

    return new_action(player, spaces)
