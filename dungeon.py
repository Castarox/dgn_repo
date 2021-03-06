import sys, tty, termios, os, random
from kamil import *
import start_game
from  termcolor import cprint
from dun_pati import *
from loaded import *


class user_class:
    ''' class containe player info'''
    def __init__(self):
        self.row = 1
        self.column = 1
        self.map = []
        self.life = 5
        self.level = 1
        self.loot = []


player = user_class()


def getch():
    '''don't know what do but work'''
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def board(x=23, y=80):
    '''create bord and frame'''
    table = []
    for row in range(x):
        table.append([])
        for column in range(y):
            if row == 0 or row == x-1 or column == 0 or column == y-1:
                table[row].append('X')
            elif row == player.row and column == player.column:
                table[row].append('@')
            else:
                table[row].append('.')
    return table


def dot_print(element,level):
    '''print colored dot'''
    if level == 1:
        print("".join(element), end='')
    elif level == 2:
        cprint("".join(element), 'yellow', end='')
    else:
        cprint("".join(element), 'red', end='')


def wall_print(element,level):
    '''print colored wall'''
    if level == 1:
        cprint("".join(element), 'red', end='')
    elif level == 2:
        cprint("".join(element), 'green', end='')
    else:
        cprint("".join(element), 'blue', end='')


def door_print(element,level):
    '''print colored doors'''
    if level == 1:
        cprint("".join(element), 'cyan', end='')
    elif level == 2:
        cprint("".join(element), 'white', end='')
    else:
        cprint("".join(element), 'green', end='')


def print_table(table):
    ''' print table to terminal'''
    for item in table:
        for element in item:
            if element == '.':
                dot_print(element,player.level)
            elif element == 'X' or element == 'A' or element == 'I':
                wall_print(element, player.level)
            elif element == '1' or element == '2' or element == '3':
                door_print(element, player.level)
            else:
                print("".join(element), end='')
        print('')


def move(user_input, door_pass):
    '''user move function'''
    key = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
    special_character = ['X', '1', '2', '3', '$', 'A', 'I']
    doors = ['1','2','3']
    status = ''
    if user_input in key:
        if player.map[player.row + key[user_input][0]][player.column+key[user_input][1]] not in special_character:
            player.map[player.row][player.column] = '.'
            player.map[player.row + key[user_input][0] ][player.column + key[user_input][1]] = '@'
            player.row += key[user_input][0]
            player.column += key[user_input][1]
        elif player.map[player.row + key[user_input][0]][player.column+key[user_input][1]] in doors:
            status = game_or_not(player.row + key[user_input][0], player.column+key[user_input][1], player.map, door_pass, player.level)
        elif player.map[player.row + key[user_input][0]][player.column+key[user_input][1]] == '$':
            boss_fight(player.life)
    elif user_input == 'l':
        player.life = operate_inventory(player.loot,player.life)
    if user_input == "\\":
            exit()
    elif user_input == "-":
        player.level += 1
        create_level()
    elif user_input == "h":
        start_game.helpp()
    if status == 'level pass':
        player.level += 1
        create_level()
    elif status == 'Losse':
        player.life -= 1
    if player.life < 1:
        start_game.game_over()
        time.sleep(3)
        exit()


def boss(board):
    '''put boss on map'''
    while True:
        x = random.randrange(1,23)
        y = random.randrange(1,80)
        if str(board[x][y]) == '.':
            board[x][y] = '$'
            break
    return board


def random_item():
    '''random set items on map'''
    i = 0
    count = 1
    item_position = []
    items = ['a','b','c','d','e']
    while True:
        x = random.randrange(19)
        y = random.randrange(59)
        if str(player.map[x][y]) == '.':
            player.map[x][y] = items[i]
            item_position.append([x, y])
            i += 1
        if i == 5:
            break
    return item_position


def ass_no_save():
    ''' new game assigment'''
    player.row = 12
    player.column = 1
    player.map = board()
    player.map = obstacle(player.level, player.map)
    player.map = doors(23, 80, player.map, player.level)
    item_position = random_item()
    return item_position


def ass_save(status_save):
    '''save game assigment'''
    status_save = load()
    player.map = status_save[0]
    hero = status_save[1]
    player.row = hero[0]
    player.column = hero[1]
    player.level = status_save[2]
    player.loot = status_save[3]
    item_position = status_save[4]
    player.life = status_save[5]
    return item_position


def create_level(status_save = 0):
    '''create game level and map during move'''
    os.system('clear')
    heart = 0
    if status_save == 0:
        item_position = ass_no_save()
    else:
        item_position = ass_save(status_save)
    door_pass = random.randrange(1,4)
    if player.level == 3:
        player.map = boss(player.map)
    print_table(player.map)
    print('Life:')
    for heart in range(player.life):
        cprint('♡', 'green', end=' ')
    print('')
    while True:
        user_input = getch()
        move(user_input, door_pass)
        os.system('clear')
        print_table(player.map)
        print('Life:')
        for heart in range(player.life):
            cprint('♡', 'green', end=' ')
        print('')
        place = [player.row, player.column]
        if place in item_position:
            what = item_position.index(place)
            what_found = find_object(what, player.loot)
            item_position.pop(what)
            player.loot = add_to_inventory(what_found, player.loot)
        if user_input == "=":
            print(user_input)
            save(player.loot, player.map, place, player.level, item_position, player.life)
        print(door_pass)


def main():
    '''main function'''
    player.loot = [rope, onion, dagger]
    rope.amount = 1
    onion.amount = 3
    dagger.amount = 1
    save_count = start_game.start()
    print(save_count != 0)
    if save_count != 0:
        create_level(save_count)
    else:
        create_level()


if __name__=='__main__':
    main()
