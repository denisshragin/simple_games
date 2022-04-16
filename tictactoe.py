

import random

def draw_board(board):


	print(' ' + board[7] + "  |  " + board[8] + "  |  " + board[9])
	print('- - - - - - - - ')
	print(' ' + board[4] + "  |  " + board[5] + "  |  " + board[6])
	print('- - - - - - - -')
	print(' ' + board[1] + "  |  " + board[2] + "  |  " + board[3])
	print('- - - - - - - -')

def choose_player_letter():
	# Ask a player to choose a symbol to play 'X' or 'O'
	# Return a list of player's and computer's letters
	letter = ''
	while letter not in ['X', 'O']:
		print("Choose a lettre X or O.")
		letter = input().upper()

	# The first element of the list is a symbol of a player, a second - of a computer
	if letter == "X":
		return ['X', 'O']
	else:
		return ['O', 'X']
	
def who_goes_first():
	# A random generator who goes first: 0-player, 1-computer
	if random.randint(0,1) == 0:
		return "Computer"
	else:
		return "Player"

def make_move(board, letter, move):
	board[move] = letter

def is_winner(board, letter):
	# Return True if letter is win

	return ((board[7]==letter and board[8]==letter and board[9]==letter) or
	(board[4]==letter and board[5]==letter and board[6]==letter) or
	(board[1]==letter and board[2]==letter and board[3]==letter) or
	(board[1]==letter and board[4]==letter and board[7]==letter) or
	(board[2]==letter and board[5]==letter and board[8]==letter) or
	(board[3]==letter and board[6]==letter and board[9]==letter) or
	(board[1]==letter and board[5]==letter and board[9]==letter) or
	(board[7]==letter and board[5]==letter and board[3]==letter))

def get_board_copy(board):
	# copy the board in the board_copy list
	board_copy = []
	for i in board:
		board_copy.append(i)
	return board_copy

def is_space_free(board, move):
	# Return True if the choosen place is free
	return board[move] == " "

def get_player_move(board):
	# Ask a player to choose a number to play
	move = ' '
	while move not in '1 2 3 4 5 6 7 8 9'.split() or not is_space_free(board, int(move)):
		print("Ou places-tu ta marque ? (1-9)")
		move = input()
	return int(move)

def choose_random_move_from_list(board, moves_list):
	# Return a valide place to move selon the state of the game
	# Return None if there are no any free place to play
	possible_moves = []
	for i in moves_list:
		if is_space_free(board, i):
			possible_moves.append(i)

	if len(possible_moves) != 0:
		return random.choice(possible_moves)
	else:
		return None

def get_computer_move(board, computer_letter):
	# Determine a computer's choice
	if computer_letter == "X":
		player_letter = "O"
	else:
		player_letter = "X"

	# An algorithm of an artificial intelligence
	# 1. Verify if computer can win with this move
	for i in range(1, 10):
		board_copy = get_board_copy(board)
		if is_space_free(board_copy, i):
			make_move(board_copy, computer_letter, i)
		if is_winner(board_copy, computer_letter):
			print("Computer goes on " + str(i))
			return i
	# 2. Verify if computer can block a player if he can in with the next move
	for i in range(1, 10):
		board_copy = get_board_copy(board)
		if is_space_free(board_copy, i):
			make_move(board_copy, player_letter, i)
			if is_winner(board_copy, player_letter):
				print("Computer goes on " + str(i))
				return i
	
	move = choose_random_move_from_list(board, [1, 3, 7, 9])
	if move != None :
		print("Computer goes on " + str(move))
		return move

	if is_space_free(board, 5):
		print("Computer goes on 5")
		return 5

	return choose_random_move_from_list(board, [2,4,6,8])

def is_board_full(board):
	# Return True if there are no a free place to play
	for i in range (1,10):
		if is_space_free(board, i):
			return False
	return True

print("Welcome to the game tic-tac-toe!")

while True:
	# Initialize the game
	board = [" "] * 10
	player_letter, computer_letter = choose_player_letter()
	turn = who_goes_first()
	print(turn + " goes first")
	game_is_playing = True

	while game_is_playing:
		if turn == "Player":
			#Tour de joueur
			draw_board(board)
			move = get_player_move(board)
			make_move(board, player_letter, move)
			print("Player letter is " + player_letter + " , computer letter is " + computer_letter)

			if is_winner(board, player_letter):
				draw_board(board)
				print("Bravo!, tu as gagne!")
				game_is_playing = False
			else:
				if is_board_full(board):
					draw_board(board)
					print("Personne ne gagne!")
					break
				else:
					turn = "Computer"
		else:
			#Tour de l'ordinateur
			move = get_computer_move(board, computer_letter)
			make_move(board, computer_letter, move)

			if is_winner(board, computer_letter):
				draw_board(board)
				print("Computer win!")
				game_is_playing = False

			else:
				if is_board_full(board):
					draw_board(board)
					print("Persone ne gagne!")
					break
				else:
					turn = "Player"

	print("Do you want to play again (Yes or No) ?")
	if not input().lower().startswith('y'):
		break






# player = choose_lettre()
# print(player)

draw_board(board)
