from dao.game import GameDao
from exceptions import GameNotFoundException
from services.board import BoardService
from services.dice import DiceService


class GameService:
    def create(self, id, board_id, dice_id, players):
        # Create board and dice
        return GameDao().create(id, board_id, dice_id, players)

    def get_by_id(self, id):
        try:
            GameDao().get_by_id(id)
        except GameNotFoundException as e:
            print("Error: ", str(e))
            return None

    def start(self, game_id):
        game = GameDao().get_by_id(game_id)

        board = BoardService().get_by_id(game.board_id)
        dice = DiceService().get_by_id(game.dice_id)
        players = game.players
        player_turn_queue = players.copy()
        cells = board.cells

        user_pos = {}

        winner = None

        for player_id in players:
            user_pos[player_id] = 0

        while True:
            curr_player = player_turn_queue.pop(0)
            player_turn_queue.append(curr_player)
            curr_pos = user_pos[curr_player]
            jump = dice.roll()
            next_pos = curr_pos + jump

            if next_pos > board.size:
                continue

            if next_pos == board.size:
                message = f"{curr_player} WON!"
                print(message)
                winner = curr_player
                break

            if cells[next_pos] != -1:
                next_pos = cells[next_pos]
                if next_pos > curr_pos:
                    print("Ladder")
                else:
                    print("Snake")

            user_pos[curr_player] = next_pos
            print(curr_player, " rolled a ", jump, " and moved from ", curr_pos, " to ", next_pos)
        return winner
