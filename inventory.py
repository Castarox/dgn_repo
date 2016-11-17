from operator import attrgetter
from termcolor import cprint

def display_inventory(inventory):
    if not inventory:
        inventory=[]
        max_board = 55
    else:
        max_key = max(inventory, key=attrgetter('name'))
        max_board = len(max_key.name)+55

    total_amount = 0
    total_weight = 0
    max_length_key = '12'
    print(inventory)

    print('Your inventory')
    cprint('='*max_board,'yellow')
    print('{:>{length_value}} {:>{length_value}} {:>{length_value}} {:>{length_value}}'.format('Item Name',
        'Weight','Amount','Total weight',length_value=max_length_key))
    for object in inventory:
        name = object.name
        weight = object.weight
        amount = object.amount
        total_weight_item = weight * amount
        total_weight += total_weight_item
        total_amount += amount
        print('{:>{length_value}} {:>{length_value}} {:>{length_value}} {:>{length_value}}'.format(name,
            weight, amount,total_weight_item,length_value=max_length_key))
    print('\n')
    print('Total items amount {} Total items weight: {}'.format(total_amount,
        total_weight))
    cprint('=' * max_board, 'yellow')

