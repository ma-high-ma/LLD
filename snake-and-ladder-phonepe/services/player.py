from dao.player import PlayerDao


class PlayerService:
    def create_player(self, id, name):
        return PlayerDao().create(id, name)
