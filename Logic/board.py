from Logic import action
from Logic import exception

from itertools import product

EMPTY_SPACE = '-'


class Board:
    def __init__(self, actions, players, width=8, height=8):
        self.width = width
        self.height = height
        self.players = players
        self.actions = actions
        self.board = self._generate_empty_board()
        self._assign_starting_positions()

    def __str__(self):
        return "Board:\n{board}".format(board=self.board)

    def _generate_empty_board(self):
        board = dict(
            zip(
                product(range(self.width), range(self.height)), EMPTY_SPACE*self.width*self.height
            )
        )
        return board

    def _assign_starting_positions(self):
        for player in self.players:
            if self.board[player.current_position] == '-':
                self.board[player.current_position] = player.character
            else:
                raise exception.InvalidPositionException("Starting player position needs to be an empty space.")

    def run_next_action(self):
        if not self.actions:
            raise exception.OutOfActionsException()

        next_action = self.actions.pop(0)
        last_player = action.perform_action(next_action, self.width, self.height)
        self._check_collision(last_player)
        self._update_board(last_player.current_position, last_player.character)

    def run_all_actions(self):
        while self.actions:
            try:
                self.run_next_action()
            except exception.PlayerCollisionException as ex:
                self.players.remove(ex.args[1])
                print(ex.args[1].name, "Out!")
                if self.players == 1:
                    break

    def _update_board(self, position, character):
        self.board[position] = character

    def _check_collision(self, player):
        if self.board[player.current_position] not in (EMPTY_SPACE, player.character):
            raise exception.PlayerCollisionException("Player Collision", player)
