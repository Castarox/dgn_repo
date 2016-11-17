import random


def random_number():

    number = random.sample(range(0, 10), 3)

    while number[0] == 0:
        pass
    else:
        return tuple(number)


def guess_number():
    while True:
        try:
            guess = input("Guess 3-digit number: ")
            if 100 < int(guess) < 1000:
                guess = list(map(int, guess))
                return tuple(guess)
            else:
                print("You are suppose to guess a 3-DIGIT NUMBER. Try again.")
        except:
            print("You are suppose to guess a 3-DIGIT NUMBER. Try again.")
            pass


def main():

    number = random_number()
    tries_left = 10
    print(number)

    while tries_left > 0:
        guess = guess_number()

        if number == guess:  # if player guesses the number
            print("HOT HOT HOT You win!")
            break

        if not set(guess) & set(number):
            print("Cold")  # if the number is totally different from random
            tries_left -= 1
            continue

        if guess[0] == number[0] and guess[1] == number[1] and not guess[2] == number[2]:
            print("Hot Hot")  # if 2 digits of player's number fit
            tries_left -= 1
            continue

        if not guess[0] == number[0] and guess[1] == number[1] and guess[2] == number[2]:
            print("Hot Hot")  # if 2 digits of player's number fit
            tries_left -= 1
            continue

        if guess[0] == number[0] and not guess[1] == number[1] and guess[2] == number[2]:
            print("Hot Hot")  # if 2 digits of player's number fit
            tries_left -= 1
            continue

        if guess[0] == number[0] or guess[1] == number[1] or guess[2] == number[2]:
            print("Hot")  # if 1 digit of player's number fits
            tries_left -= 1
            continue

        if set(guess) & set(number):
            print("Warm")  # if player inserted number that contains digit(s) of random
            tries_left -= 1
            continue

    print("No more guesses left. You lost.")


main()
