the_board = {7: '   ', 8: '   ', 9: '   ',
             4: '   ', 5: '   ', 6: '   ',
             1: '   ', 2: '   ', 3: '   '}

# status whether game continue or not
game_still_continue = True
# who won or draw?
winner = None
# which player's turn is it?
current_player = " O "

def display_board():
    print(the_board[7] + '|' + the_board[8] + '|' + the_board[9])
    print('---|---|---')
    print(the_board[4] + '|' + the_board[5] + '|' + the_board[6])
    print('---|---|---')
    print(the_board[1] + '|' + the_board[2] + '|' + the_board[3])

# operate each function from here
def play_game():
    # pass
    # display board for tic-tac-toe at first
    display_board()

    # loop continue until game finishes
    while game_still_continue:
        # call function to input your favorite number
        enter_turn(current_player)
        # call function to check if game finished
        check_if_win_lose()
        # call function to change to the other player
        change_player()

    # When game finished
    if winner == " O " or winner == " X ":
        print(f"Congratulations!{winner}You won!")
    elif winner == None:
        print("It's a draw")

# input your favorite number
def enter_turn(player):
    # pass
    position = int(input(f"[{player}] Please make your move! [1-9]: "))

    # when impossible input was done
    valid = False
    while not valid:
        # error message appears when you input except following numbers
        while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            print("Invalid Input! Please enter a number!")
            play_game()
        # error message appears when you input existing number on the board
        if the_board[position] != '   ':
            print("Invalid move! Please try again!")
            play_game()
        else:
            valid = True

    the_board[position] = player
    display_board()

def check_if_win_lose():
    check_if_win()
    check_if_draw()


def check_if_win():
    global winner

    # check rows
    row_winner = check_rows()

    # check columns
    column_winner = check_columns()

    # check diagonals
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    return

def check_if_draw():
    # pass
    global game_still_continue
    value_list = list(the_board.values())

    if '   ' not in value_list:
        game_still_continue = False
    return

def check_rows():
    global game_still_continue

    row_1 = the_board[7] == the_board[8] == the_board[9] != '   '
    row_2 = the_board[4] == the_board[5] == the_board[6] != '   '
    row_3 = the_board[1] == the_board[2] == the_board[3] != '   '

    if row_1 or row_2 or row_3:
        game_still_continue = False
    if row_1:
        return the_board[7]
    elif row_2:
        return the_board[4]
    elif row_3:
        return the_board[1]
    return

def check_columns():
    global game_still_continue

    column_1 = the_board[7] == the_board[4] == the_board[1] != '   '
    column_2 = the_board[8] == the_board[5] == the_board[2] != '   '
    column_3 = the_board[9] == the_board[6] == the_board[3] != '   '

    if column_1 or column_2 or column_3:
        game_still_continue = False
    if column_1:
        return the_board[7]
    elif column_2:
        return the_board[8]
    elif column_3:
        return the_board[9]
    return

def check_diagonals():
    global game_still_continue

    diagonal_1 = the_board[7] == the_board[5] == the_board[3] != '   '
    diagonal_2 = the_board[9] == the_board[5] == the_board[1] != '   '

    if diagonal_1 or diagonal_2:
        game_still_continue = False
    if diagonal_1:
        return the_board[7]
    elif diagonal_2:
        return the_board[9]
    return

def change_player():
    global current_player

    if current_player == " O ":
        current_player = " X "
    elif current_player == " X ":
        current_player = " O "
    return

print("Tic-Tac-Toe!")
print("Player 1 is O and Player 2 is X.")
play_game()