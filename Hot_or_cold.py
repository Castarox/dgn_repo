import random

def number_generator():
    number = random.randrange(100,999)
    number = str(number)
    return number


def check_win(user_input, number):
    if user_input == number:
        return True
    else:
        return False

def check(user_input, number):
    counter = 0
    hot = []
    for i in range(len(number)):
        if number[i] == user_input[i]:
                print('hot', end=' ')
                hot.append(i)
                counter += 1
    for i in range(len(number)):
        if i not in hot and user_input[i] in number:
            print('warm', end=' ' )
            counter += 1
    if counter == 0:
        print("cold")


def main():
    print('I am thinking of a 3-digit number. Try to guess what it is.')
    print('Here are some clues:')
    print('When I say: \t That means:')
    print("{:>2} {:>12}".format("Cold","No digit is correct."))
    random_number = number_generator()
    print(random_number)
    guess_count = 1
    while True:
        user_input = input("\nGuess #%d:\n" % (guess_count))
        if len(user_input) != 3 or not user_input.isdigit():
            print("wrong input")
            continue
        win = check_win(user_input, random_number)
        if win == True:
            break
        check(user_input, random_number)
        if guess_count == 10:
            break 
        guess_count += 1


if __name__ == '__main__':
    main()