from collections import deque

from dao.game import GameDao
from exceptions import GameNotFound
from services.board import BoardService


class GameService:
    def create(self, id, player_id, board_id):
        return GameDao().create(id, player_id, board_id)

    def start_game(self, game_id):
        try:
            game = GameDao().get_by_id(id=game_id)
        except GameNotFound as e:
            print(str(e))
            return None
        board = BoardService().get_by_id(id=game.board_id)
        x = self.find_jumps(board.cells)
        print("min jumps = ", x)
        return x

    def find_jumps(self, cells):
        q = []
        n = len(cells)
        q.append([0, 0])  # cell_index, throws
        minThrows = 99999
        visited = set()
        visited.add((0, 0))

        while q:

            curr_cell_index, throws = q.pop(0)
            for dice in range(1, 7):
                next_index = curr_cell_index + dice

                if next_index >= n:
                    continue

                if next_index == n - 1:
                    minThrows = min(throws + 1, minThrows)
                    continue

                if cells[next_index] == -1:
                    next_index = next_index
                else:
                    cell_val = cells[next_index]
                    next_index = cell_val - 1

                if (next_index, throws + 1) not in visited:
                    q.append([next_index, throws + 1])
                    visited.add((next_index, throws + 1))

        return minThrows if minThrows != 99999 else -1
