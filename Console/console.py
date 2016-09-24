import Logic

from operator import itemgetter


class Console:
    def __init__(self):
        parsed = Logic.parser.parse_action_file('actions.json')
        self.board = Logic.board.Board(action_list, players)
