from exceptions import GameNotFound
from models.game import Game


class GameDao:
    GameMap = {}

    def get_by_id(self, id):
        try:
            return self.GameMap[id]
        except KeyError:
            raise GameNotFound(id)

    def create(self, id, player_id, board_id):
        game = Game(id=id, player_id=player_id, board_id=board_id, minimum_throws=-1)
        self.GameMap[game.id] = game
        return game
