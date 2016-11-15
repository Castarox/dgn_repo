from termcolor import colored
welcome_file = 'welcome.txt'
credits_file = 'credits.txt'
help_file = 'help.txt'


def start():
	welcome()
	display_menu()
	while True:
		command = input('Enter command :')
		if command == '1':
			break
		elif command == '2':
			credits()
		elif command == '3':
			help()
		elif command == '4':
			exit()
		else:
			print('Wrong command')


def welcome():
	with open(welcome_file, 'r') as content:
		text = content.read()
		print(colored(text,'red'))

def credits():
	with open(credits_file, 'r') as content:
		text = content.read()
		print(colored(text, 'green'))
		print('Peter: Design & Menu')
		print('')

def help():
	with open(help_file, 'r') as content:
		text = content.read()
		print(colored(text, 'green'))
		print('To move hero use A,D,W,S')
		print()


def display_menu():
	print('Start Game press 1')
	print('Credits press 2')
	print('Help press 3')
	print('Quit game press 4')