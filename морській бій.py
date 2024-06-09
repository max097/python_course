#SEA BATTLE

import random
import time
WATER_CELL = "~"
SHIP_CELL = "H"
MISSED_CELL = "o"
HIT_CELL = "X"
SHIPS_FOR_PLAYER = 1
FIELD_LETTERS = "A"




def fill_field(field, ship_cell, ships_f_p):

    for i in range(ships_f_p):
        while True:
            random_key = random.choice(list(field.keys()))
            random_value = random.randint(0, len(list(field.keys()))-1)
            if field[random_key][random_value] == ship_cell:
                continue
            else:
                field[random_key][random_value] = ship_cell
                break
    return field



def create_field(letters, water):
    field = dict()
    for x in letters:
        field[x] = []
        for i in range(len(letters)):
            field[x].append(water)



    return field

def ship_counter(field, ship_c):
    counter = 0
    for lst in list(field.values()):
        for value in lst:
            if value == ship_c:
                counter += 1
    return counter
def game_continue(p_field, c_field, ship_c):
    p_counter = ship_counter(p_field, ship_c)
    c_counter = ship_counter(c_field, ship_c)
    if p_counter and c_counter:
        return True
    else:
        return False

def print_one_field(field, ship_c, is_visible = True):
    num = '  '
    for x in range(len(field)):
        num += str(x) + " "
    print(num)
    for key in list(field.keys()):
        st = f"{key} "
        for value in field[key]:
            if value == ship_c and is_visible == False:
                st += "~" + " "
            else:
                st += value + " "
        print(st)


def display_board(p_field, c_field, p_ships, c_ships, ship_cell):
    print("\n--- SEA BATTLE ---\n")
    time.sleep(1)
    print("\n   PLAYER FIELD")
    print_one_field(p_field, ship_cell, True)
    time.sleep(1)
    print("\n   COMPUTER FIELD")
    print_one_field(c_field, ship_cell, False)
    time.sleep(1)
    print(f'''\n\nSTATISTICS:
    Player ships - {p_ships}
    Computer ships - {c_ships}''')


def player_shoots(letters, comp_field, m_cell, h_cell):
    numbers = '  '
    for x in range(len(letters)):
        numbers += str(x)
    while True:
        u_inp = input("Куди будемо стріляти? ").upper()
        if len(u_inp) == 0:
            print("Ви нічого не ввели")
            continue
        elif len(u_inp) != 2:
            print("Введіть 2 символа")
            continue
        elif u_inp[0] not in letters or \
             u_inp[1] not in numbers:
            print("Ви ввели некоректні дані")
            continue
        if comp_field[u_inp[0]][int(u_inp[1])] == m_cell or \
            comp_field[u_inp[0]][int(u_inp[1])] == m_cell:
            print("Ви вже стріляли в цю ячейку")
            continue
        else:
            return u_inp


def comp_shooting(letters, p_field, m_cell, h_cell):
    while True:
        r_letter = random.choice(letters)
        r_number = random.randint(0, len(letters)-1)
        if p_field[r_letter][r_number] == m_cell or \
                p_field[r_letter][r_number] == h_cell:
            continue
        else:
            return r_letter + str(r_number)

def analitics(field, shot, s_cell, m_cell, h_cell):
    letter = shot[0]
    number = int(shot[1])
    if field[letter][number] == s_cell:
        print("ПОПАДАННЯ")
        field[letter][number] = h_cell
    else:
        print("ПРОМАХ")
        field[letter][number] = m_cell
    return field

def game(water_cell, ship_cell, missed_cell, hit_cell, ships_f_p, letters):
    player_field = create_field(letters, water_cell)
    comp_field = create_field(letters, water_cell)

    player_field = fill_field(player_field, ship_cell, ships_f_p)
    comp_field = fill_field(comp_field, ship_cell, ships_f_p)


    while game_continue(player_field, comp_field, ship_cell):
        display_board(
            player_field,
            comp_field,
            ship_counter(player_field, ship_cell),
            ship_counter(comp_field, ship_cell),
            ship_cell
        )

        player_shot = player_shoots(letters, comp_field, missed_cell, hit_cell)
        print(f"\nГравець стріляє в {player_shot}")

        comp_field = analitics(comp_field, player_shot, ship_cell, missed_cell, hit_cell)
        time.sleep(1)

        comp_shots = comp_shooting(letters, player_field, missed_cell, hit_cell)
        print(f"\nКомпютер стріляє стріляє в {comp_shots}")
        player_field = analitics(player_field, comp_shots, ship_cell, missed_cell, hit_cell)
        time.sleep(1)
    winner = ''
    if ship_counter(player_field, ship_cell) > ship_counter(comp_field, ship_cell):
        winner = "PLAYER"
    elif ship_counter(player_field,ship_cell) < ship_counter(comp_field,ship_cell):
        winner = 'COMPUTER'
    else:
        winner = 'DRAW'
    print(f'''
    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    {winner} WINS!
    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
    ~ ~ ~ ~ ~ ~ ~ ~ ~ ~
''')





print("SEA BATTLE")
game(WATER_CELL, SHIP_CELL, MISSED_CELL,HIT_CELL, SHIPS_FOR_PLAYER, FIELD_LETTERS)
print("THANKS FOR PLAYING")