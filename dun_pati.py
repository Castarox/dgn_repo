import random
from operator import attrgetter
from termcolor import cprint
import os


class Stuff():
''' class contain items can appear on map'''
    def __init__(self, name, weight, st_type, sign):
        self.name = name
        self.weight = weight
        self.st_type = st_type
        self.sign = sign
        self.amount = 3


'''creat object of items '''
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
    '''chech what object was found'''
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
    return loot


def totalweight(loot):
    """Counts sum of all items in inventory"""
    total_amount = sum([item.weight*item.amount for item in loot])
    print('Total weight of items: %s\n' % total_amount)
    return total_amount


def operate_inventory(inventory, player_life=10):
    ''' mange inventory operations'''
    display_inventory(inventory, player_life)
    player_life_value = player_life
    while True:
        command = input('Commands: Drop Items [d], switch to game [l],add some health points[h] ')
        if command == 'd':
            player_life_value = drop_item(inventory,player_life_value)
        elif command == 'h':
            player_life_value = life_safer(inventory, player_life_value)
        elif command == 'l':
            os.system('clear')
            return player_life_value
        else:
            print('Uknown command')


def display_inventory(inventory,player_life):
    ''' show inventory'''
    os.system('clear')
    if not inventory:
        inventory=[]
        max_board = 55
    else:
        max_key = max(inventory, key=attrgetter('name'))
        max_board = len(max_key.name)+86
    total_amount = 0
    total_weight = 0
    max_length_key = '12'
    print('Your inventory')
    cprint('='*max_board,'yellow')
    print('   {:>{length_value}} {:>{length_value}} {:>{length_value}} {:>{length_value}}'.format('Item Name',
        'Weight','Amount','Total weight',length_value='20'))
    for i,object in enumerate(inventory,start=1):
        name = object.name
        weight = object.weight
        amount = object.amount
        total_weight_item = weight * amount
        total_weight += total_weight_item
        total_amount += amount
        print('{}. {:>{length_value}} {:>{length_value}} {:>{length_value}} {:>{length_value}}'.format(i,name,
            weight, amount,total_weight_item,length_value='20'))
    print('\n')
    print('Total items amount {} Total items weight: {} Ilość żyć {}'.format(total_amount,
        total_weight,player_life))
    cprint('=' * max_board, 'yellow')


def  drop_item(inventory,player_life):
    '''drop items from inv'''
    while True:
        drop = input('Which item you want to drop,enter index of item, x to quit')
        if drop == 'x':
            print('All set check your inventory')
            display_inventory(inventory, player_life)
            return  player_life
        try:
            drop_int = int(drop)
        except:
            print('You cannot pass string , only [x], please try again')
            pass
        if int(drop_int):
            count = int(input('How many do you want to drop?'))
            ele = inventory[drop_int-1]
            print('Ilość poczatkowa',ele.amount)
            if ele.amount > count and count >= 0:
                ele.amount -= count
            elif ele.amount <= count:
                inventory.pop(drop_int - 1)
                print('You haven no more {}'.format(ele.name))
            else:
                print('Something went wrong please try again')
            display_inventory(inventory, player_life)
            return player_life


def  life_safer(inventory,player_life):
    ''' switch item to live'''
    while True:
        eat = input('Which item you want to eat to restore your life!!!')
        if eat == 'x':
            break
        try:
            eat_int = int(eat)
        except:
            print('You cannot pass string , only [x], please try again')
            pass
        print('Player Life',player_life)
        if int(eat_int):
            count = int(input('How many do you want to eat?'))
            ele = inventory[eat_int-1]
            if ele.amount > count and count >= 0:
                ele.amount -= count
                player_life_extra = player_life + (count*2)
                display_inventory(inventory, player_life_extra)
                return player_life_extra
            elif ele.amount <= count:
                inventory.pop(eat_int - 1)
                print('You haven no more {}'.format(ele.name))
                player_life_extra = player_life + (ele.amount * 2)
                display_inventory(inventory,player_life_extra)
                return player_life_extra
            else:
                print('Something went wrong please try again')


def save(loot, boardxy, hero, level, items_position, life):
    '''save game to file'''
    name = input("Enter your name to personalize your save: ")
    import os
    #os.system('touch %d_save.csv' % name)
    with open('save/%s_save.csv' % (name), 'w') as sfile:
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
    with open('save/list.csv', 'a') as name_file:
        name_file.write('%s\n' % name)
    exit()
