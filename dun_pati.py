import random
from operator import attrgetter
from termcolor import cprint
import os


class Stuff():

    def __init__(self, name, weight, st_type, sign):
        self.name = name
        self.weight = weight
        self.st_type = st_type
        self.sign = sign
        self.amount = 1


onion = Stuff('onion', 2, 'food', 'a')
carrot = Stuff('carrot', 3, 'food', 'b')
hat = Stuff('hat', 5, 'clothes', 'c')
goat = Stuff('goat', 0, 'other', 'd')
knife = Stuff('knife', 5, 'weapons', 'e')
rope = Stuff('rope', 10, 'other', 'e')
torch = Stuff('torch', 10, 'other', 'e')
gold = Stuff('gold', 15, 'other', 'e')
dagger = Stuff('dagger', 5, 'weapon', 'e')
arrow = Stuff('arrow', 5, 'weapon', 'e')


def obstacle(level, board_obst, amount=10, size=8):
    """Prints random obstacles on board"""

    if level == 1:
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
    elif level == 2:
        disper = 7
        yy = 7
        for n in range(amount):
            rock_x = random.randint(2,22 - size)
            rock_y = random.randint(yy, disper)
            ran_size = random.randrange(3, 9, 2)
            for n in range(ran_size): # 0, 1, 2
                for m in range(n): # 0
                    board_obst[rock_x + n][rock_y + m] = "A"
                    board_obst[rock_x + n][rock_y - m] = "A"
            disper += 7
            yy += 7
    elif level == 3:
        for n in range(2,79):
            for m in range(random.randrange(3, 11, 2)): # 0, 1, 2
                board_obst[m][n] = "I"
        for n in range(2,79):
            for m in range(random.randrange(3, 11, 2)):
                board_obst[22 - m][n] = "I"

    return board_obst


def find_object(what, loot):
    #whole = [onion, carrot, hat, goat, knife, rope, torch, gold, dagger, arrow]
    whole = [onion, hat]
    found_object = random.choice(whole)
    print("You found %s" % found_object.name)
    return found_object



def add_to_inventory(item, loot):
    """Add new items to inventory"""
    total_weight = totalweight(loot) + item.weight
    if total_weight > 30:
        print("to much shit, You must drop something")
    else:
        if item in loot:
            item.amount += 1
        else:
            loot.append(item)
            item.amount = 1
        print("\n***Inventory upgraded***\n")
        print("You have %d %s" %(item.amount, item.name))
    #totalweight(loot)
    return loot


def totalweight(loot):
    """Counts sum of all items in inventory"""
    total_amount = sum([item.weight*item.amount for item in loot])
    print('Total weight of items: %s\n' % total_amount)
    return total_amount

def display_inventory(inventory):

    os.system('clear')
    if not inventory:
        inventory=[]
        max_board = 55
    else:
        max_key = max(inventory, key=attrgetter('name'))
        max_board = len(max_key.name)+55

    total_amount = 0
    total_weight = 0
    max_length_key = '12'
    print('Your inventory')
    cprint('='*max_board,'yellow')
    print('{:>{length_value}} {:>{length_value}} {:>{length_value}} {:>{length_value}}'.format('Item Name',
        'Weight','Amount','Total weight',length_value=max_length_key))

    for i,object in enumerate(inventory,start=1):
        name = object.name
        weight = object.weight
        amount = object.amount
        total_weight_item = weight * amount
        total_weight += total_weight_item
        total_amount += amount
        print('{}. {:>{length_value}} {:>{length_value}} {:>{length_value}} {:>{length_value}}'.format(i,name,
            weight, amount,total_weight_item,length_value=max_length_key))
    print('\n')
    print('Total items amount {} Total items weight: {}'.format(total_amount,
        total_weight))
    cprint('=' * max_board, 'yellow')
    command = input('Commands: Drop Items [d], switch to game l ')

    # if command == 'd':
    #
    # else:
    #     print('Go go play')


def save(loot, boardxy, hero, level, items_position, life):
    name = input("Enter your name to personalize your save: ")
    import os
    #os.system('touch %d_save.csv' % name)
    with open('%s_save.csv' % (name), 'w') as sfile:
        for line in boardxy:
            for point in line:
                sfile.write('%s,' %(point))
            sfile.write('\n')
        sfile.write('hero,%s,%s\n' %(hero[0], hero[1]))
        sfile.write('level,%s\n' % (level))
        sfile.write('items_position, %s\n' % str(items_position))
        sfile.write('Life, %d\n' % (life))
        for item in loot:
            sfile.write('%s,%d,%s,%d\n' %(item.name, item.weight, item.st_type, item.amount))

    exit()
