import sys, tty, termios, os, random
from kamil import *
import start_game
from  termcolor import cprint
from dun_pati import *

class user_class:
    def __init__(self):
        self.row = 1
        self.column = 1
        self.map = []
        self.life = 5
        self.level = 1
        self.loot = []


player = user_class()

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def board(x=23, y=80):
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
    if level == 1:
        print("".join(element), end='')
    elif level == 2:
        cprint("".join(element), 'yellow', end='')
    else:
        cprint("".join(element), 'red', end='')


def wall_print(element,level):
    if level == 1:
        cprint("".join(element), 'red', end='')
    elif level == 2:
        cprint("".join(element), 'green', end='')
    else:
        cprint("".join(element), 'blue', end='')


def door_print(element,level):
    if level == 1:
        cprint("".join(element), 'cyan', end='')
    elif level == 2:
        cprint("".join(element), 'white', end='')
    else:
        cprint("".join(element), 'green', end='')


def drukowanie_tablicy(table):
    for item in table:
        for element in item:
            if element == '.':
                dot_print(element,player.level)
            elif element == 'X':
                wall_print(element, player.level)
            elif element == '1' or element == '2' or element == '3':
                door_print(element, player.level)
            else:
                print("".join(element), end='')
        print('')

def move(user_input, door_pass):
    key = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
    special_character = ['X','1','2','3','$']
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
        display_inventory(player.loot)
    else:
        exit()
    print(player.life)
    print(status)
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
    while True:
        x = random.randrange(1,23)
        y = random.randrange(1,80)
        if str(board[x][y]) == '.':
            board[x][y] = '$'
            break
    return board


def random_item():
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

def create_level():
    heart = 0
    door_pass = random.randrange(1,4)
    player.row = 12
    player.column = 1
    player.map = board()
    player.map = obstacle(player.level, player.map)
    player.map = doors(23, 80, player.map, player.level)
    item_position = random_item()
    if player.level == 3:
        player.map = boss(player.map)
    drukowanie_tablicy(player.map)
    print('Life:')
    for heart in range(player.life):
        cprint('♡', 'green', end=' ')
    print('')
    while True:
        user_input = getch()
        move(user_input, door_pass)
        os.system('clear')
        drukowanie_tablicy(player.map)
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
        print(door_pass)

def main():
    player.loot = [rope, onion, dagger]
    start_game.start()
    create_level()
    
    
    


if __name__=='__main__':
    main()