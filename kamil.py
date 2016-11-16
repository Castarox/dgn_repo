import random, os
from termcolor import colored
import game

def doors(row, column, board):
    door_number = 1
    for i in range(3):
        x = random.randrange(1,5)
        if x == 1:
            position = random.randrange(1,column-1)
            board[0][position] = str(door_number)
        elif x == 2:
            position = random.randrange(1,column-1)
            board[row-1][position] = str(door_number)
        elif x == 3:
            position = random.randrange(1,row-1)
            board[position][0] = str(door_number)
        else:
            position = random.randrange(1,row-1)
            board[position][column-1] = str(door_number)
        door_number += 1
    return board


def game_or_not(row, column, map, door_pass):

    lista = ['a','b','c','d','e']
    print(map[row][column])
    print(map[row][column] == door_pass)
    if map[row][column] == str(door_pass) and map[row][column] not in lista:
        print('level pass')
        return 'level pass'
    elif map[row][column] != '.' and map[row][column] not in lista and map[row][column] != 'x':
        os.system('clear')
        game.main()
