import os
import random
from kamil import *
import start_game
from dun_pati import *
from  termcolor import cprint
from inventory import *

def getch():
    """Reads one character without enter"""
    import sys, tty, termios
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def print_board(board):
    """Prints board"""

    for row in board:
        for element in row:
            if element == '.':
                print("".join(element),end='')
            elif element == 'X':
                cprint("".join(element),'green',end='')
            elif element == '1' or element == '2' or element == '3':
                cprint("".join(element), 'red', end='')
            else:
                print("".join(element), end='')
        print('')


def board(boardxy, x = 23, y = 80):
    """Creates board"""
    boardxy = []
    for row in range(x):
        boardxy.append([])
        for column in range(y):
            if row == 0 or row == 22 or column == 0 or column == 79:
                boardxy[row].append("X")
            else:
                boardxy[row].append(".")

    #boardxy[position[0]][ position[1]] = "@"
    return boardxy


def hero_position(position, boardxy):
    boardxy[position[0]][ position[1]] = "@"
    return boardxy



def move(step, position, boardxy, door_pass, loot, level):
    status = ''
    if step == "d": #move right
        if boardxy[position[0]][position[1]+1] == "X":
            return position
        else:
            status = game_or_not(position[0], position[1]+1, boardxy, '2')
            boardxy[position[0]][position[1]] = "."
            position[1] += 1

    if step == "a": #move left
        if boardxy[position[0]][position[1]-1] == "X":
            return position
        else:
            status = game_or_not(position[0], position[1]-1, boardxy, '2')
            boardxy[position[0]][position[1]] = "."
            position[1] -= 1
    if step == "w": #move up
        if boardxy[position[0]-1][position[1]] == "X":
            return position
        else:
            status = game_or_not(position[0]-1, position[1], boardxy, '2')
            boardxy[position[0]][position[1]] = "."
            position[0] -= 1
    if step == "s": #move down
        if boardxy[position[0]+1][position[1]] == "X":
            return position
        else:
            status = game_or_not(position[0]+1, position[1], boardxy, '2')
            boardxy[position[0]][position[1]] = "."
            position[0] += 1
    if status == 'level pass':

        level += 1
        create_level(level, loot)

    else:
        return position


def random_item(boardxy, items_position):
    i = 0
    count = 1
    items = ['a','b','c','d','e']
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



def create_level(level, loot):
    print(level)
    print('\n\n\n\n\n\n\n\n')

    items_position = []
    hero = [12, 1]
    door_pass = random.randrange(1,4)
    start_board = []
    start_board = board(start_board)
    start_board = hero_position(hero, start_board)
    start_board = obstacle(level, start_board)
    start_board = random_item(start_board, items_position)
    doors(23,80, start_board)
    print_board(start_board)
    game_board = start_board[:]

    while True:
        # os.system('clear')
        print_board(game_board)
        display_inventory(loot)
        y = getch()

        hero = move(y, hero, game_board, door_pass,loot, level)
        hero_position(hero, game_board)
        if hero in items_position:
            what = items_position.index(hero)

            found = find_object(what)
            items_position.pop(what)
            loot = add_to_inventory(found, loot)

        if y == "\\":
            exit()

def main ():

    loot = []

    level = 1
    start_game.start()
    create_level(level, loot)

    #print(id(game_board), id(start_board))




if __name__ == "__main__":
   main()
