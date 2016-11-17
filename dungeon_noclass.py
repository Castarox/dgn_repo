import os
import random
from kamil import *
import start_game
from dun_pati import *
from termcolor import cprint
from inventory import *


def getch():
    """Reads one character without enter"""
    import sys
    import tty
    import termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def level1(element, level):
    if level == 1:
        print("".join(element), end='')
    elif level == 2:
        cprint("".join(element), 'yellow', end='')
    else:
        cprint("".join(element), 'red', end='')


def level2(element, level):
    if level == 1:
        cprint("".join(element), 'red', end='')
    elif level == 2:
        cprint("".join(element), 'green', end='')
    else:
        cprint("".join(element), 'blue', end='')


def level3(element, level):
    if level == 1:
        cprint("".join(element), 'cyan', end='')
    elif level == 2:
        cprint("".join(element), 'white', end='')
    else:
        cprint("".join(element), 'green', end='')


def print_board(board, level=1):
    """Prints board"""
    print('Akutalny level', level)
    for row in board:
        for element in row:
            if element == '.':
                level1(element, level)
            elif element == 'X':
                level2(element, level)
            elif element == '1' or element == '2' or element == '3':
                level3(element, level)
            else:
                print("".join(element), end='')
        print('')


def board(boardxy, x=23, y=80):
    """Creates board"""
    boardxy = []
    for row in range(x):
        boardxy.append([])
        for column in range(y):
            if row == 0 or row == 22 or column == 0 or column == 79:
                boardxy[row].append("X")
            else:
                boardxy[row].append(".")
    return boardxy


def hero_position(position, boardxy):
    boardxy[position[0]][position[1]] = "@"
    return boardxy


def move(x, position, boardxy, door_pass, loot, level):
    key = {"w": (-1, 0), "s": (1, 0), "a": (0, -1), "d": (0, 1)}
    special_character = ['X', '1', '2', '3', '$']
    doors = ['1', '2', '3']
    status = ''
    if x in key:
        if boardxy[position[0] + key[x][0]][position[1] + key[x][1]] not in special_character:
            boardxy[position[0]][position[1]] = '.'
            boardxy[position[0] + key[x][0]][position[1] + key[x][1]] = '@'
            position[0] += key[x][0]
            position[1] += key[x][1]
        elif boardxy[position[0] + key[x][0]][position[1] + key[x][1]] in doors:
            status = game_or_not(position[0] + key[x][0], position[1] + key[x][1], boardxy, door_pass, level)
        elif boardxy[position[0] + key[x][0]][position[1] + key[x][1]] == '$':
            status = game_or_not(position[0] + key[x][0], position[1] + key[x][1], boardxy, door_pass, level)
    if status == 'level pass':
        level += 1
        create_level(level, loot)
    return position


def random_item(boardxy, items_position):
    i = 0
    count = 1
    items = ['a', 'b', 'c', 'd', 'e']
    while True:
        x = random.randrange(19)
        y = random.randrange(78)
        if boardxy[x][y] == '.':
            boardxy[x][y] = items[i]
            items_position.append([x, y])
            i += 1
        if i == 5:
            break
    return boardxy


def boss(board):
    while True:
        x = random.randrange(1, 23)
        y = random.randrange(1, 80)
        if str(board[x][y]) == '.':
            board[x][y] = '$'
            break
    return board


def create_level(level, loot):
    print(level)
    print('\n\n\n\n\n\n\n\n')
    items_position = []
    hero = [12, 1]
    door_pass = random.randrange(1, 4)
    print(door_pass)
    start_board = []
    start_board = board(start_board)
    start_board = hero_position(hero, start_board)
    start_board = obstacle(level, start_board)
    start_board = random_item(start_board, items_position)
    doors(23, 80, start_board, level)
    print_board(start_board)
    game_board = start_board[:]
    if level == 3:
        game_board = boss(game_board)
    while True:
        os.system('clear')
        print_board(game_board, level)
        display_inventory(loot)
        user_move = getch()
        hero = move(user_move, hero, game_board, door_pass, loot, level)
        hero_position(hero, game_board)
        if hero in items_position:
            what = items_position.index(hero)
            found = find_object(what, loot)
            items_position.pop(what)
            loot = add_to_inventory(found, loot)
        if user_move == "\\":
            exit()


def main():
    loot = [rope, onion, dagger]
    level = 1
    start_game.start()
    create_level(level, loot)


if __name__ == "__main__":
    main()
