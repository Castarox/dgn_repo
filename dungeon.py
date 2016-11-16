import sys, tty, termios, os, random
from kamil import *
import start_game

class user_class:
    def __init__(self):
        self.row = 1
        self.column = 1
        self.map = []
        self.life = 5


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


def tablica(x=20, y=60):
    lista = []  
    for rzad in range(x):
        lista.append([])
        for kolumn in range(y):
            if rzad == 0 or rzad == x-1 or kolumn == 0 or kolumn == y-1: 
                lista[rzad].append('x')
            elif rzad == player.row and kolumn == player.column:
                lista[rzad].append('@')
            elif rzad in range(5,10) and kolumn in range(5,10):
                lista[rzad].append('x')
            elif rzad in range(14,19) and kolumn in range(12,20):
                lista[rzad].append('x')
            elif rzad in range(5,13) and kolumn in range(35,45):
                lista[rzad].append('x')
            else:
                lista[rzad].append('.')
    return lista


def drukowanie_tablicy(lista):
    for i in lista:
        print(''.join(i))

def move(user_input, door_pass):
    if user_input == 'a':
        player.column -= 1
        status = game_or_not(player.row, player.column, player.map, door_pass)
        if player.map[player.row][player.column] == '.':
            player.map[player.row][player.column] = '@'
            player.map[player.row][player.column+1] = '.'
        else:
            player.column +=1
    elif user_input == 'd':
        player.column += 1
        status = game_or_not(player.row, player.column, player.map, door_pass)
        if player.map[player.row][player.column] == '.':
            player.map[player.row][player.column] = '@'
            player.map[player.row][player.column-1] = '.'
        else:
            player.column -= 1
    elif user_input == 'w':
        player.row -= 1
        status = game_or_not(player.row, player.column, player.map, door_pass)
        if player.map[player.row][player.column] == '.':
            player.map[player.row][player.column] = '@'
            player.map[player.row+1][player.column] = '.'
        else:
            player.row += 1
    elif user_input == 's':
        player.row += 1
        status = game_or_not(player.row, player.column, player.map, door_pass) 
        if player.map[player.row][player.column] == '.':
            player.map[player.row][player.column] = '@'
            player.map[player.row-1][player.column] = '.'
        else:
            player.row -= 1
    else:
        sys.exit()
    if status == 'level pass':
        create_level()

def random_item():
    i = 0
    count = 1
    items = ['a','b','c','d','e']
    while True:
        x = random.randrange(19)
        y = random.randrange(59)
        if player.map[x][y] == '.':
            player.map[x][y] = items[i]
            i += 1
        if i == 5:
            break


def create_level():
    door_pass = random.randrange(1,4)
    player.map = tablica()
    player.map = doors(20, 60, player.map)
    random_item()
    drukowanie_tablicy(player.map)
    while True:
        user_input = getch()
        move(user_input, door_pass)
        #os.system('clear')
        drukowanie_tablicy(player.map)
        print(door_pass)

def main():
    start_game.start()
    create_level()
    
    
    


if __name__=='__main__':
    main()