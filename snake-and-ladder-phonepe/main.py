from services.board import BoardService
from services.game import GameService
from services.player import PlayerService

if __name__ == '__main__':
    """
    Input:
    Total number of rows : 3
    Cells : -1 3 -1
    Cells : -1 5 -1
    Cells : -1 -1 9
    
    Output:
    [-1, 3, -1, -1, 5, -1, -1, -1, 9]
    min jumps =  2
    """
    print("Begin")
    n = int(input("Total number of rows : "))
    cells = []
    for i in range(n):
        row = input("Cells : ")
        row = list(row.split(" "))
        row = [int(i) for i in row]
        cells += row

    print(cells)
    board = BoardService().create_board(id="b0", rows=n, cells=cells)
    player = PlayerService().create_player(id="p0", name="player 0")
    game = GameService().create(id="g0", player_id=player.id, board_id=board.id)
    GameService().start_game(game_id=game.id)
