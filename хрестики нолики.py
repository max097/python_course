import random
import time
def inp_letter():
    u_inp = ''
    while u_inp not in ["X", "O"]:
        u_inp = input("Виберіть X або O - ").upper()
    if u_inp == "X":
        return "X", "O"
    else:
        return "O", "X"


def first_turn():
    if random.randint(0, 1) == 0:
        return "PLAYER"
    else:
        return "COMPUTER"
def display_board(board):
    print(f'''
        {board[1]}|{board[2]}|{board[3]}
        -+-+-
        {board[4]}|{board[5]}|{board[6]}
        -+-+-
        {board[7]}|{board[8]}|{board[9]}
''')

def is_cell_free(board, move):
    return board[int(move)] == " "
def get_player_move(board):
    p_move = " "
    while p_move not in "1 2 3 4 5 6 7 8 9".split() or not is_cell_free(board, p_move):
        p_move = input("Куди ходимо? (1-9) ")
        if not is_cell_free(board, p_move):
            print("Ця ячейка вже зайнята")
    return int(p_move)





def make_move(board, move, letter):
    board[move] = letter
    return board
def is_winner(bo, le):
    if (bo[1] == le and bo[2] == le and bo[3] == le) or \
        (bo[4] == le and bo[5] == le and bo[6] == le) or \
        (bo[7] == le and bo[8] == le and bo[9] == le) or \
        (bo[1] == le and bo[4] == le and bo[7] == le) or \
        (bo[2] == le and bo[5] == le and bo[8] == le) or \
        (bo[3] == le and bo[6] == le and bo[9] == le) or \
        (bo[1] == le and bo[5] == le and bo[9] == le) or \
        (bo[3] == le and bo[5] == le and bo[7] == le):
        return True
    else:
        return False
def get_comp_move(board, c_letter, p_letter):
    #win
    for i in range(1, 10):
        if board[i] == " ":
            board_copy = board[:]
            board_copy[i] = c_letter
            if is_winner(board_copy, c_letter):
                return i


    #no lose
    for i in range(1, 10):
        if board[i] == " ":
            board_copy = board[:]
            board_copy[i] = p_letter
            if is_winner(board_copy, p_letter):
                return i

    #center
    if board[5] == " ":
        return 5
    #corners
    lst = []
    for x in [1, 3, 7, 9]:
        if board[x] == " ":
            lst.append(x)
    if len(lst) > 0:
        return random.choice(lst)
    #straight
    lst = []
    for x in [2, 4, 6, 8]:
        if board[x] == " ":
            lst.append(x)
    if len(lst) > 0:
        return random.choice(lst)

def is_board_full(board):
    for i in range(1, 10):
        if board[i] == ' ':
            return False
    return True
def game():
    board = [" "] * 10
    player_letter, comp_letter = inp_letter()
    turn = first_turn()
    print(f"{turn} робить перший хід")
    game_is_running = True
    while game_is_running:
        if turn == "PLAYER":
            display_board(board)
            p_move = get_player_move(board)
            board = make_move(board, p_move, player_letter)
            if is_winner(board, player_letter):
                display_board(board)
                print("ГРАВЕЦЬ ВИГРАВ!")
                game_is_running = False

            else:
                if is_board_full(board):
                    display_board(board)
                    print("НІЧИЯ")
                    game_is_running = False
                else:
                    turn = "COMPUTER"



        else:
            comp_move = get_comp_move(board, comp_letter, player_letter)
            board = make_move(board, comp_move, comp_letter)
            if is_winner(board, comp_letter):
                display_board(board)
                print("КОМПУТЕР ВИГРАВ!")
                game_is_running = False
            if is_board_full(board):
                display_board(board)
                print("НІЧИЯ")
                game_is_running = False
            turn = "PLAYER"





print("--- ХРЕСТИКИ НОЛИКИ ---")
game()
print("ДЯКУЄМО ЗА ГРУ!")