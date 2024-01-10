from dao.board import BoardDao
from exceptions import BoardNotFound


class BoardService:
    BoardMap = {}

    def create_board(self, id, rows, cells):
        board = BoardDao().create(id, rows, cells)
        self.BoardMap[board.id] = board
        return board

    def get_by_id(self, id):
        try:
            return self.BoardMap[id]
        except KeyError:
            raise BoardNotFound(id)

