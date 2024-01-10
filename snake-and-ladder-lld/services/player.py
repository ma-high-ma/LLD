from dao.player import PlayerDao
from exceptions import PlayerNotFoundException


class PlayerService:
    def create(self, id, name):
        return PlayerDao().create(id, name)
    
    def get_by_id(self, id):
        try:
            PlayerDao().get_by_id(id)
        except PlayerNotFoundException as e:
            print("Error: ", str(e))
            return None
