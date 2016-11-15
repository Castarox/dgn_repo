import random, os
from termcolor import colored
import game

def doors(row, column, board):
    door_number = 1
    for i in range(3):
        x = random.randrange(1,5)
        if x == 1:
            position = random.randrange(1,column-1)
            board[0][position] = str(colored(door_number,'red'))
        elif x == 2:
            position = random.randrange(1,column-1)
            board[row-1][position] = str(colored(door_number,'green'))
        elif x == 3:
            position = random.randrange(1,row-1)
            board[position][0] = str(colored(door_number,'yellow'))
        else:
            position = random.randrange(1,row-1)
            board[position][column-1] = str(colored(door_number,'blue'))
        door_number += 1


def game_or_not(row, column, map, door_pass):
    print(map[row][column])
    print(door_pass)
    if map[row][column] == str(door_pass):
        print('level pass')
        return 'level pass'
    elif map[row][column] == 1 or map[row][column] == 3 :
        os.system('clear')
        game.main()

