from termcolor import colored
import dungeon
import os
welcome_file = 'welcome.txt'
credits_file = 'credits.txt'
help_file = 'help.txt'


def start():
	"""os.system('clear')
	welcome()
	display_menu()"""
	while True:
		os.system('clear')
		welcome()
		display_menu()
		command = input('Enter command :')
		if command == '1':
			save_count = 0
			break
		elif command == '2':
			credits()
		elif command == '3':
			helpp()
		elif command == '4':
			exit()
		elif command == '5':
			save_count = 1
			break
		else:
			print('Wrong command')
	return save_count

def welcome():
	with open(welcome_file, 'r') as content:
		text = content.read()
		print(colored(text,'red'))

def credits():
	os.system('clear')
	with open(credits_file, 'r') as content:
		text = content.read()
		print(colored(text, 'green'))
		input("Enter - back to menu")

def helpp():
	os.system('clear')
	with open(help_file, 'r') as content:
		text = content.read()
		print(colored(text, 'green'))
		input("Enter - back to menu or game")
		

def win_game():
	with open('win_game.txt', 'r') as content:
		text = content.read()
		print(colored(text, 'yellow'))

def game_over():
	with open('game_over.txt', 'r') as content:
		text = content.read()
		print(colored(text, 'red'))
		print()

def display_menu():
	print('Start Game press 1')
	print('Credits press 2')
	print('Help press 3')
	print('Quit game press 4')
	print('Load saved game: 5')
