from dun_pati import *
from inventory import *
from kamil import *


"""def drukowanie_tablicy(lista):
    for i in lista:
        print(''.join(i))"""

def load():
    with open('save/list.csv', 'r') as ll:
        print(ll.read())
        name = input("Choose your user: ")
    with open('save/%s_save.csv' %name, 'r') as lfile:
        boardxy = [row.strip("\n") for row in lfile]

    board = []
    hero = []
    row = []
    lev = []
    loott = []
    loot = []
    position =[]

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


    for i, row in enumerate(boardxy):
        if i >= 26:
            item = []
            for pole in row.split(","):
                item.append(pole)
            loott.append(item)

    print(loott)

    for item in loott:
        item[0] = Stuff(item[0], int(item[1]), item[2], int(item[3]))
        loot.append(item[0])
        print()


    return board, hero, level, loot, position
