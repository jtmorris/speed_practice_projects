import numpy as np
from random import randint






def generate_blank_board():
	return np.zeros((3,3))

def completed_slice(slice):
	"""Checks if all values of the list are the same."""
	last_s = None
	for s in slice:
		if s == 0: # Not filled in yet. No winner
			return False
		else:
			if last_s and last_s != s:
				return False
			else:
				last_s = s

	return True

def any_winners(board):
	"""Checks all win paths to see if there is a winner.

	Parameters:
		board: A 2D NumPy array representing a tic tac toe board.

	Returns:
		int: The integer code representing the winner.
	"""
	slices = (
		board.diagonal(),            # Diagonal #1
		np.fliplr(board).diagonal(), # Diagonal #2
		board[0],                    # Horizontal top row
		board[1],                    # Horizontal middle row
		board[2],                    # Horizontal bottom row
		board[:,0],                  # Vertical left row
		board[:,1],                  # Vertical middle row
		board[:,2]                   # Vertical right row
	)

	for s in slices:
		if completed_slice(s):
			print(s)
			return s[0]

	return None

def code_to_char(code: int) -> str:
	if code == -1:
		return 'O'
	elif code == 1:
		return 'X'
	elif code == 0:
		return ' '
	else:
		raise ValueError("Invalid character code. Only -1 and 1 are allowed.")

def valid_coordinates(user_input_coords):
	inp = user_input_coords.split(',')

	if len(inp) != 2:
		raise ValueError("Invalid coordinates. Requires 2 comma separated values.")

	if int(inp[0]) > 3:
		raise ValueError("Invalid y (vertical) coordinate. Not on board.")

	if int(inp[1]) > 3:
		raise ValueError("Invalid x (horizontal) coordinate. Not on board.")

	return True


def print_board(board):
	# Column header
	cols = board.shape[1]
	c = 1
	print("     ", end='') # Space for row headers
	horiz_border = "-----"
	while c <= cols:
		print("|  " + str(c) + "  ", end='')
		horiz_border = horiz_border + "|-----"
		c = c + 1
	print("\n" + horiz_border)
	r = 1
	for y in board:
		print("  " + str(r) + "  ", end='')
		horiz_border = "-----"
		for x in y:
			print("|  " + code_to_char(x) + "  ", end='')
			horiz_border = horiz_border + "|-----"
		print("\n" + horiz_border)

		r = r + 1


board = generate_blank_board()
gi = 0 # Game counter. Resets on each new game.
while True:
	# If this is a new game, set it up and pick a first player
	if gi == 0:
		board = generate_blank_board()
		who_goes = (-1, 1)[randint(0,1)]
		print_board(board)
		print('"' + code_to_char(who_goes) + '" goes first.')
		gi = gi + 1

	# If this is iteration 9 on the game counter, then there have been
	# no winners and no spaces should be remaining. So it's a draw.
	if gi == 10:
		input("Draw. Press <Enter> to play another game.")
		gi = 0
		continue

	# Prompt for user input
	ui = input('"' + code_to_char(who_goes) + '", enter your desired coordinate (y,x), or type "q" to quit:  ')

	# Quit option
	if ui == 'q':
		break

	# Validate user input.
	try:
		valid_coordinates(ui)
	except ValueError:
		print("Invalid coordinates or command, pick again.")
		continue

	# Make sure spot is available
	ucs = ui.split(',')
	ucs = [int(uc)-1 for uc in ucs] # Cast to int and address 0 indexed array and 1 indexed input
	if board[ucs[0],ucs[1]] != 0:
		print("That spot is already taken by " + code_to_char(board[ucs[0],ucs[1]]) + '. Try again.')
		continue

	# Toggle spot
	board[ucs[0],ucs[1]] = who_goes

	# Check for win
	if any_winners(board) != None:
		print_board(board)
		input("WINNER! Congratulations. Press <Enter> to play another game.")
		gi = 0
		continue

	# Change whose turn it is
	who_goes = -1 * who_goes

	# Increment game counter
	gi = gi + 1

	# Show the board
	print_board(board)