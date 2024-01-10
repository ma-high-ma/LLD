from exceptions import PlayerNotFoundException
from models.player import Player


class PlayerDao:
    PlayerMap = {}

    def get_by_id(self, id):
        try:
            return self.PlayerMap[id]
        except KeyError:
            raise PlayerNotFoundException

    def create(self, id, name):
        player = Player(id, name)
        self.PlayerMap[id] = player
        return player
