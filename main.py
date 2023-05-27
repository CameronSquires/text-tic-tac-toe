def check_for_win(current_player, board, game_end):
    first_row_win = board[0] == board[1] == board[2] != " "
    second_row_win = board[3] == board[4] == board[5] != " "
    third_row_win = board[6] == board[7] == board[8] != " "
    first_column_win = board[0] == board[3] == board[6] != " "
    second_column_win = board[1] == board[4] == board[7] != " "
    third_column_win = board[2] == board[5] == board[8] != " "
    first_diagonal_win = board[0] == board[4] == board[8] != " "
    second_diagonal_win = board[2] == board[4] == board[6] != " "

    if first_row_win:
        print(f"Winner is {board[0]}\n")
        play_game(current_player, True, board)
    
    if second_row_win:
        print(f"Winner is {board[3]}\n")
        play_game(current_player, True, board)

    if third_row_win:
        print(f"Winner is {board[6]}\n")
        play_game(current_player, True, board)
    
    if first_column_win:
        print(f"Winner is {board[0]}\n")
        play_game(current_player, True, board)
    
    if second_column_win:
        print(f"Winner is {board[1]}\n")
        play_game(current_player, True, board)
    
    if third_column_win:
        print(f"Winner is {board[2]}\n")
        play_game(current_player, True, board)
    
    if first_diagonal_win:
        print(f"Winner is {board[0]}\n")
        play_game(current_player, True, board)
    
    if second_diagonal_win:
        print(f"Winner is {board[2]}\n")
        play_game(current_player, True, board)

    
def game_draw(board, current_player, game_end):
    print("Game ended in a draw!\n")

    play_game(current_player, game_end, board)

def check_game_win_draw(current_player, board, game_end):
    check_for_win(current_player, board, game_end)
    if " " not in board:
        game_draw(board, current_player, True)
    

    

def play_turn(current_player, game_end, board):
    tile_choice = input(f"Which tile would player {current_player} like to play?: ")
    try:
        tile_choice = int(tile_choice)
        tile_choice -= 1
        if (0 <= tile_choice <= 8) and board[tile_choice] == " ":
            board[tile_choice] = current_player
        else:
            print("Please input a valid tile.")
            play_turn(current_player, board)
    except:
        print("Please input a valid tile.")
        play_turn(current_player, board)


def play_game(current_player, game_end, board):
    if game_end == True:
        rematch = input("Would you like to have a rematch?: ")
        if rematch == "yes":
            start_game()
        else:
            exit()
    while not game_end:
        play_turn(current_player, game_end, board)
        board_visual = f"""
 {board[0]} | {board[1]} | {board[2]}
-----------
 {board[3]} | {board[4]} | {board[5]}
-----------
 {board[6]} | {board[7]} | {board[8]}
"""
        print(board_visual)
        check_game_win_draw(current_player, board, game_end)
        if current_player == "x":
            current_player = "o"
        else:
            current_player = "x"


def basics():
    input("""
--------------------------------------------------------------------
Please pick who is X and who is O.
X will go first, then O, following this pattern until the game ends.
Press ENTER to continue.
--------------------------------------------------------------------""")
    options()
def options():
    player_options = input("""
--------------------------------------------------------------------
Type 'help' if you need help regarding how the grid works.
Type 'tutorial' for the rules of the game.
Type 'play' if you'd like to start playing.
--------------------------------------------------------------------

""")

    if player_options.lower() == "help":
        input("""
--------------------------------------------------------------------
To play, on your turn, type a number 1-9 corresponding to the tile on the grid you'd like to place your piece on.
the number for each tile is as follows:

 1 | 2 | 3
-----------
 4 | 5 | 6
-----------
 7 | 8 | 9

Press ENTER to continue.
--------------------------------------------------------------------""")
        options()

    if player_options.lower() == "tutorial":
        input("""
        
--------------------------------------------------------------------
The X player starts by placing an X on the board, followed by the O player playing an O, repeating until the game is over.
A player wins if their tile is in 3 tiles in a row. Horizontally, vertically or diagonally
If all tiles are filled and no player has won, the game ends in a draw.

Press ENTER to continue.
--------------------------------------------------------------------""")
        options()

    if player_options.lower() == "play":
        start_game()
def start_game():
    board=[' ', ' ', ' ',
            ' ', ' ', ' ',
            ' ', ' ', ' ']
    current_player = 'x'
    game_end = False
    play_game(current_player, game_end, board)

basics()