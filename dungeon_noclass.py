import os
import random


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
        print("".join(row))


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


def obstacle(board_obst, amount=10, size=8):
    """Prints random obstacles on board"""
    disper = 7
    yy = 2
    for n in range(amount):
        rock_x = random.randint(4,22 - size)
        rock_y = random.randint(yy, disper)
        ran_size = random.randint(4, size)
        for n in range(ran_size):
            for m in range(ran_size):
                board_obst[rock_x + n][rock_y + m] = "X"
        disper += 7
        yy += 7
    return board_obst


def hero_position(position, boardxy):
    boardxy[position[0]][ position[1]] = "@"
    return boardxy


def move(step, position, boardxy):
    if step == "d": #move right
        if boardxy[position[0]][position[1]+1] == "X":
            return position
        else:
            boardxy[position[0]][position[1]] = "."
            position[1] += 1

    if step == "a": #move left
        if boardxy[position[0]][position[1]-1] == "X":
            return position
        else:
            boardxy[position[0]][position[1]] = "."
            position[1] -= 1
    if step == "w": #move up
        if boardxy[position[0]-1][position[1]] == "X":
            return position
        else:
            boardxy[position[0]][position[1]] = "."
            position[0] -= 1
    if step == "s": #move down
        if boardxy[position[0]+1][position[1]] == "X":
            return position
        else:
            boardxy[position[0]][position[1]] = "."
            position[0] += 1

    return position


def random_item(boardxy):
    i = 0
    count = 1
    items = ['a','b','c','d','e']
    while True:
        x = random.randrange(19)
        y = random.randrange(59)
        if boardxy[x][y] == '.':
            boardxy[x][y] = items[i]
            i += 1
        if i == 5:
            break
    return boardxy

def main ():

    items_position = []
    hero = [12, 1]
    start_board = []
    start_board = board(start_board)
    start_board = hero_position(hero, start_board)
    start_board = obstacle(start_board)
    start_board = random_item(start_board)
    print_board(start_board)
    game_board = start_board[:]
    #print(id(game_board), id(start_board))

    while True:
        os.system('clear')
        print_board(game_board)
        y = getch()
        hero = move(y, hero, game_board)
        hero_position(hero, game_board)
        if y == "\\":
            exit()


if __name__ == "__main__":
   main()
