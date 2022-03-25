board = [1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9]
####################################################################
def display_board():
    print("|" , board[0] , "|" , board[1] , "|" , board[2] , "|")
    print("------------")
    print("|" , board[3] , "|" , board[4] , "|" , board[5] , "|")
    print("------------")
    print("|" , board[6] , "|" , board[7] , "|" , board[8] , "|")
#####################################################################
def get_input(player):
    valid_move = False
    note = "Enter The position you want player" + player + ":"
    while not valid_move:
        move = input(note)
        if move.isdigit():
            valid_move = True
            move = int(move)
            valid_move = valid_move and move > 0 and move <= 9
            valid_move = valid_move and board[move - 1] != "X" and board[move - 1] != "O"
    return move
########################################################################
def update_board(move , player):
    board[move - 1] = player
    display_board()
########################################################################
def is_winner():
    row1 = (board[0] == board[1]) and (board[0] == board[2])
    row2 = (board[3] == board[4]) and (board[3] == board[5])
    row3 = (board[6] == board[7]) and (board[6] == board[8])
    col1 = (board[0] == board[3]) and (board[0] == board[6])
    col2 = (board[1] == board[4]) and (board[1] == board[7])
    col3 = (board[2] == board[5]) and (board[2] == board[8])
    shape1 = (board[0] == board[4]) and (board[0] == board[8])
    shape2 = (board[2] == board[4]) and (board[2] == board[6])
    return row1 or row2 or row3 or col1 or col2 or col3 or shape1 or shape2
###########################################################################
def play_game():
    display_board()
    number_of_moves = 0
    while number_of_moves != 9:
        move = get_input("X")
        update_board(move , "X")
        if is_winner():
            print("Player X Won:)")
            break
        number_of_moves += 1
        if number_of_moves == 9:
            break
        move = get_input("O")
        update_board(move , "O")
        if is_winner():
            print("Player O won:)")
            break
        number_of_moves += 1
    if not is_winner():
        print("Draw:(")
play_game()        