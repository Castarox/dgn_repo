import random
from termcolor import cprint


def number_generator():
    '''generate rundom number'''
    numer_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    a = random.choice(numer_list)
    numer_list.remove(a)
    b = random.choice(numer_list)
    numer_list.remove(b)
    c = random.choice(numer_list)
    numer_list.remove(c)
    number = '%s%s%s'%(a, b, c)
    print(number)
    return number


def check_win(user_input, number):
    '''match random number with user number'''
    if user_input == number:
        return True
    else:
        return False


def check(user_input, number):
    '''print hot cold or warm'''
    counter = 0
    hot = []
    for i in range(len(number)):
        if number[i] == user_input[i]:
            print('Hot', end=' ')
            hot.append(i)
            counter += 1
    for i in range(len(number)):
        if i not in hot and user_input[i] in number:
            print('Warm', end=' ')
            counter += 1
    if counter == 0:
        print("Cold", end=' ')


def hints_dictionary():
    '''print start game clue'''
    print("\nI am thinking of a 3-digit number. You have 10 guesses\033[1m to get it\033[0m.")  # "to get it" is bold.
    print('\nHere are some clues:\n')
    print("When I say:\tThat means:\n")

    hints_dict = {'  Cold': 'No digit is correct.', '  Warm': 'One digit is correct but in the wrong position.',
                  '  Hot': 'One digit is correct and already in the right place.'}

    for key in hints_dict:
        print ("{:<17} {}\n".format(key, hints_dict[key]))


def print_boos():
    color_table =['red', 'yellow', 'blue', 'green', 'magenta', 'cyan']
    random_color = random.randrange(0,6)
    random_color = color_table[random_color]
    with open('boss.txt', 'r') as content:
        text = content.read()
        cprint(text, random_color)

def main(life = 10):
    hints_dictionary()
    random_number = number_generator()
    print(random_number)
    guess_count = 1
    while True:
        print_boos()
        user_input = input("\n\nGuess #%d: \n" % (guess_count))
        if len(user_input) != 3 or not user_input.isdigit():
            print("Wrong input!")
            continue
        win = check_win(user_input, random_number)
        if win is True:
            print("HOT HOT HOT!\nWell done! Your guess was correct and you deafat boss")
            return 'Win'
            break
        check(user_input, random_number)
        if guess_count == life:
            print("\nYOU LOOSE!")
            return 'Game over'
            break
        guess_count += 1


if __name__ == '__main__':
    main()
