from exceptions import PlayerNotFound
from models.player import Player


class PlayerDao:
    PlayerMap = {}

    def get_by_id(self, id):
        try:
            return self.PlayerMap[id]
        except KeyError:
            raise PlayerNotFound(id)

    def create(self, id, name):
        return Player(id=id, name=name)
