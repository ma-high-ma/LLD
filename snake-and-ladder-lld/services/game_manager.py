from dao.game import GameDao
from services.board import BoardService
from services.dice import DiceService
from services.game import GameService
from services.player import PlayerService


class GameManager:

    def create_player(self, id, name):
        return PlayerService().create(id, name)

    def create_board(self, id, size, snakes, ladders):
        return BoardService().create(id, size, snakes, ladders)

    def create_dice(self, id, total_number=1):
        return DiceService().create(id, total_number)

    def create_game(self, id, board_id, dice_id, players):
        return GameService().create(id, board_id, dice_id, players)

    def start_game(self, game_id):
        return GameService().start(game_id)

