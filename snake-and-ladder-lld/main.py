from services.game_manager import GameManager

if __name__ == '__main__':

    # no_of_snakes = int(input("Number of Snakes: "))
    # snake_pos = []
    # for i in range(no_of_snakes):
    #     start, end = input("Enter start and end : ").split(" ")
    #     snake_pos.append([int(start), int(end)])
    #
    # no_of_ladders = input("Number of Ladders: ")
    # ladder_pos = []
    # for i in range(no_of_snakes):
    #     start, end = input("Enter start and end : ").split(" ")
    #     ladder_pos.append([int(start), int(end)])
    # board = GameManager().create_board(id="b0", size=100, snakes=snake_pos, ladders=ladder_pos)

    s = [[90, 80], [70, 60], [50, 40]]
    l = [[20, 30], [45, 55], [75, 95]]

    board = GameManager().create_board(id="b0", size=100, snakes=s, ladders=l)

    # no_of_players = int(input("Number of Players: "))
    no_of_players = 2
    players = []
    for i in range(no_of_players):
        # name = input("Name: ")
        id = f"p{i}"
        player = GameManager().create_player(id=id, name="ABC")
        players.append(player.id)

    dice = GameManager().create_dice(id="d0")
    game = GameManager().create_game(id="g0", board_id=board.id, dice_id=dice.id, players=players)
    GameManager().start_game(game.id)





