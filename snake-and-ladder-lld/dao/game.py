from exceptions import GameNotFoundException
from models.game import Game


class GameDao:
    GameMap = {}

    def get_by_id(self, id):
        try:
            return self.GameMap[id]
        except KeyError:
            raise GameNotFoundException

    def create(self, id, board_id, dice_id, players):
        game = Game(id, board_id, dice_id, players, user_position={})
        self.GameMap[game.id] = game
        return game
