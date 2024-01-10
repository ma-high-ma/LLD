class BoardNotFoundException(Exception):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"{self.id} -> Board Not Found"


class DiceNotFoundException(Exception):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"{self.id} -> Dice Not Found"


class GameNotFoundException(Exception):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"{self.id} -> Game Not Found"


class PlayerNotFoundException(Exception):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"{self.id} -> Player Not Found"
