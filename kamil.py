import random, os
from termcolor import colored
import game

def doors(row, column, board, level):
    door_number = 1
    if level < 3:
        for i in range(3):
            x = random.randrange(1,5)
            if x == 1:
                position = random.randrange(1,column-1)
                board[0][position] = str(door_number)
            elif x == 2:
                position = random.randrange(1,column-1)
                board[row-1][position] = str(door_number)
            elif x == 3:
                position = random.randrange(1,row-1)
                board[position][0] = str(door_number)
            else:
                position = random.randrange(1,row-1)
                board[position][column-1] = str(door_number)
            door_number += 1
    return board


def game_or_not(row, column, map, door_pass, level):
    lista = ['a','b','c','d','e']
    if map[row][column] == str(door_pass) and map[row][column] not in lista:
        return 'level pass'
    elif map[row][column] != '.' and map[row][column] not in lista and map[row][column] != 'x':
        os.system('clear')
        if level == 1:
            game.main()
        elif level == 2:
            rock_paper()


def rock_paper():
    player_points = 0
    computer_points = 0
    options = ['rock', 'scissors', 'paper']
    victory = 0
    while True:
        user_choice = input('What you chosse: Rock(1), Scissors(2), Paper(3) ')
        try:
            int(user_choice)
        except ValueError:
            print('Wrong input')
        else:
            if 0<int(user_choice)<4 and user_choice.isdigit(): 
                computer_choice = random.randrange(1,4)
                computer_choice = str(computer_choice)
                user_choice = str(user_choice)
                if user_choice == computer_choice:
                    print('Draw !')
                elif user_choice == '1' and computer_choice == '2':
                    print('You Win !')
                    player_points += 1
                elif user_choice == '1' and computer_choice == '3':
                    print ('You Losse')
                    computer_points += 1
                elif user_choice == '2' and computer_choice == '3':
                    print('You Win !')
                    player_points += 1
                elif user_choice == '2' and computer_choice == '1':
                    print ('You Losse')
                    computer_points += 1
                elif user_choice == '3' and computer_choice == '1':
                    print('You Win !')
                    player_points += 1
                elif user_choice == '3' and computer_choice == '2':
                    print ('You Losse')
                    computer_points += 1
                print(player_points)
                print(computer_points)
            else:
                print('wrong input')
        if player_points == 3:
            print('Great you win the game')
            victory = 1
            break
        elif computer_points == 3:
            print('You losse whole game !!')
            break
    if victory == 1:
        return 'Win'
    else:
        return 'Losse'
