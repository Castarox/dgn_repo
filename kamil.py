import random, os
from termcolor import colored
import game

def doors(row, column, board):
    door_number = 1
    for i in range(3):
        x = random.randrange(1,5)
        if x == 1:
            position = random.randrange(1,column-1)
            # board[0][position] = str(colored(door_number,'red'))
            board[0][position] = str(door_number)
        elif x == 2:
            position = random.randrange(1,column-1)
            # board[row-1][position] = str(colored(door_number,'green'))
            board[row-1][position] = str(door_number)
        elif x == 3:
            position = random.randrange(1,row-1)
            # board[position][0] = str(colored(door_number,'yellow'))
            board[position][0] = str(door_number)
        else:
            position = random.randrange(1,row-1)
            # board[position][column-1] = str(colored(door_number,'blue'))
            board[position][column-1] = str(door_number)
        door_number += 1


def game_or_not(row, column, map, door_pass):
    print('_' + door_pass + '_')
    print('_' + map[row][column] + '_')
    print(type(map[row][column]))
    
    print(type(door_pass))

    print((map[row][column]) == door_pass)
    print((map[row][column]) in door_pass)

    if map[row][column] == door_pass:
        print('level pass')
        return 'level pass'
    elif map[row][column] != '.':
        # os.system('clear')
        game.main()
    else:
        print('no')

