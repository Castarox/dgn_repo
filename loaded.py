from dun_pati import *
from kamil import *
import start_game
import os

def load():
    '''load from fille and return tuple'''
    print("Choose your name or 'exit' to back to menu:")
    with open('save/list.csv', 'r') as ll:
        print(ll.read())
        name = input("Choose your user: ")
        if name == "exit" or name == "EXIT":
            start_game.start()
    try:
        with open('save/%s_save.csv' %name, 'r') as lfile:
            boardxy = [row.strip("\n") for row in lfile]
    except FileNotFoundError:
        print("Wrong name")
        load()
    with open('save/%s_save.csv' %name, 'r') as lfile:
        boardxy = [row.strip("\n") for row in lfile]
    board = []
    hero = []
    row = []
    lev = []
    loott = []
    loot = []
    position =[]
    life = 0
    for i, linia in enumerate(boardxy):
        row = []
        if i == 23:
            break
        else:
            for pole in linia.split(","):
                row.append(pole)
            board.append(row)
    for pole in boardxy[23].split(",")[1:3]:
        hero.append(int(pole))
    print(hero)
    for pole in boardxy[24].split(",")[1:]:
        lev.append(int(pole))
        level = lev[0]
    print(level)
    for pole in boardxy[25].split(",")[1:]:
        position.append((pole))
    print(position)
    for pole in boardxy[26].split(",")[1:]:
        life = int(pole)
        print(life)
    for i, row in enumerate(boardxy):
        if i >= 27:
            item = []
            for pole in row.split(","):
                item.append(pole)
            loott.append(item)
    print(loott)
    for item in loott:
        item[0] = Stuff(item[0], int(item[1]), item[2], int(item[3]))
        loot.append(item[0])
        print()
    return board, hero, level, loot, position, life
