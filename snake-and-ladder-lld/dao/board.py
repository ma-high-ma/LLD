from exceptions import BoardNotFoundException
from models.board import Board


class BoardDao:
    BoardMap = {}

    def get_by_id(self, id):
        try:
            return self.BoardMap[id]
        except KeyError:
            raise BoardNotFoundException(id=id)

    def create(self, id, size, snakes, ladders):
        """
        positions: [[1, 5], [2, 3]]
        """
        cells = [-1] * (size + 1)
        self.update_cells_with_jumper_positions(cells, snakes)
        self.update_cells_with_jumper_positions(cells, ladders)
        board = Board(id=id, size=size, cells=cells)
        self.BoardMap[board.id] = board
        return board

    def update_cells_with_jumper_positions(self, cells, positions):
        for start_pos, end_pos in positions:
            cells[start_pos] = end_pos
        return cells
