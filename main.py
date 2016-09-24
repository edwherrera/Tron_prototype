from Logic.board import Board
from Logic import parser
from Logic import exception

parsed = parser.parse_action_file("actions.json")

board = Board(**parsed)


def play():
    board.run_all_actions()
    print("Remaining: ", [player.name for player in board.players])


def main():
    play()


if __name__ == '__main__':
    main()
