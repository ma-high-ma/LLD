from exceptions import BoardNotFound
from models.board import Board


class BoardDao:
    BoardMap = {}

    def get_by_id(self, id):
        try:
            return self.BoardMap[id]
        except KeyError:
            raise BoardNotFound(id)

    def create(self, id, rows, cells):
        return Board(id=id, rows=rows, cells=cells)
