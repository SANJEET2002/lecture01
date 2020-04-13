

def show_board(board):

    print(board[7] + ' | ' + board[8] + ' | ' + board[9])

    print(board[4] + ' | ' + board[5] + ' | ' + board[6])

    print(board[1] + ' | ' + board[2] + ' | ' + board[3])




def player_input():
    marker = ''
    while marker.upper() != 'X' and marker.upper() != 'O':
        marker = input("Enter Player 1 Choice Here")

        player_1 = marker
        if marker.upper() == 'X':
            player_2 = 'O'
        else:
            player_2 = 'X'

    return (player_1,player_2)


def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,marker):
    return (board[7] == board[8] == board[9] == marker or
    board[4] == board[5] == board[6] == marker or
    board[1] == board[2] == board[3] == marker or
    board[1] == board[4] == board[7] == marker or
    board[8] == board[5] == board[2] == marker or
    board[3] == board[6] == board[9] == marker or
    board[9] == board[5] == board[1] == marker or
    board[3] == board[5] == board[7] == marker)


def space_check(board,position):
    return board[position] == ' '

def full_board_space_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False

    return True

def choose_first():
    import random
    flip = random.randint(0,1)
    if flip == 0:
        return 'player_1'
    else:
        return 'player_2'

def choose_position(board):
    position = 0

    if position not in range(1,10) or not space_check(board,position):
        position = int(input('Enter The position Here (1-9)'))

        return position



def replay():
    choice = input('Want to play agian if Yes then Y or No N ').upper()

    return choice == 'Y'


while True:
    print('Welcome to TIC TAC TOE ')
    ## set the board
    the_board = [' ']*10
    player1_marker ,player2_marker = player_input()

    turn = choose_first()
    print(turn + ' Will go first ')

    play_game = input('Want to play the game Enter Y or N').upper()

    if play_game == 'Y':
        game_on = True
    else:
        game_on = False


    while game_on:
        if turn == 'player_1':
            print('player 1 Turn ')
            show_board(the_board)
            position = choose_position(the_board)
            place_marker(the_board, player1_marker, position)
            if win_check(the_board, player1_marker):
                print('player 1  Has won the Game ')
                show_board(the_board)
                game_on = False
            else:
                if full_board_space_check(the_board):
                    print(' Tie  Game!')
                    game_on = False

                else:
                    turn = 'player_2'
        else:
            if turn == 'player_2':
                print('player 2 Turn ')
                show_board(the_board)
                position = choose_position(the_board)
                place_marker(the_board, player2_marker, position)
                if win_check(the_board, player2_marker):
                    print('player 2  Has won the Game ')
                    show_board(the_board)
                    game_on = False
                else:
                    if full_board_space_check(the_board):
                        print(' Tie  Game!')
                        game_on = False

                    else:
                        turn = 'player_1'

    if not replay():
         break