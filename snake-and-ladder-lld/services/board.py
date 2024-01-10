from dao.board import BoardDao
from exceptions import BoardNotFoundException


class BoardService:
    def create(self, id, size, snakes, ladders):
        return BoardDao().create(id, size, snakes, ladders)
    
    def get_by_id(self, id):
        try:
            return BoardDao().get_by_id(id)
        except BoardNotFoundException as e:
            print("Error: ", str(e))
            return None

