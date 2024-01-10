class PlayerNotFound(Exception):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"Player {self.id} NotFound"


class BoardNotFound(Exception):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"Board {self.id} NotFound"


class GameNotFound(Exception):
    def __init__(self, id):
        self.id = id

    def __str__(self):
        return f"Game {self.id} NotFound"
