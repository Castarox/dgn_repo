import random


class Stuff():

    def __init__(self, name, weight, st_type, sign):
        self.name = name
        self.weight = weight
        self.st_type = st_type
        self.sign = sign
        self.amount = 0

onion = Stuff('onion', 2, 'food', 'a')
carrot = Stuff('carrot', 3, 'food', 'b')
hat = Stuff('hat', 5, 'clothes', 'c')
goat = Stuff('goat', 20, 'other', 'd')
knife = Stuff('knife', 5, 'weapons', 'e')
rope = Stuff('rope', 10, 'other', 'e')
torch = Stuff('torch', 10, 'other', 'e')
gold = Stuff('gold', 1, 'other', 'e')
dagger = Stuff('dagger', 5, 'weapon', 'e')
arrow = Stuff('arrow', 3, 'weapon', 'e')

"""whole = [onion, carrot, hat, goat, knife, rope, torch, gold, dagger, arrow]
items_on_board = []
for n in range(5):
    items_on_board.append(random.choice(whole))
    print(items_on_board[n].name)"""

#loot = []



#(a, b, c, d, e) = ()

def find_object(what):
    #whole = [onion, carrot, hat, goat, knife, rope, torch, gold, dagger, arrow]
    whole = [onion, hat]
    found_object = random.choice(whole)
    print("You found %s" % found_object.name)
    return found_object


def add_to_inventory(item, loot):
    """Add new items to inventory"""
    print("here ajem")
    if item in loot:
        item.amount += 1
    else:
        loot.append(item)
        item.amount = 1
    print("\n***Inventory upgraded***\n")
    print("You have %d %s" %(item.amount, item.name))
    return loot
