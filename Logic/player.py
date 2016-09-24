class Player:
    def __init__(self, name: str, starting_position: tuple, character: str = None):
        self.name = name
        self.character = character if character else name[0].lower()
        self.position = {
            'x': starting_position[0],
            'y': starting_position[1]
        }

    def __str__(self):
        return "Player: {name}({char}) @ {position}".format(name=self.name, position=self.current_position, char=self.character)

    def move(self, *, horizontal=0, vertical=0):
        self.position['x'] += horizontal
        self.position['y'] += vertical

    @property
    def current_position(self):
        return self.position['x'], self.position['y']
