import numpy as np
from random import randint

settings = {
	"num_mines": 2,
	"board_dimensions": (9, 9)
}


def get_setting(setting_name: str):
	"""Returns a settings value from the settings dictionary.

	Returns: The setting value if it exists, None if not.
	"""

	try:
		return settings[setting_name]
	except IndexError:
		return None

def random_coordinates(board_height: int, board_width: int):
	"""Returns random coordinates on a grid of specified dimensions.

	Parameters:
		board_height (int):	The grid height.
		board_width (int): The grid width.

	Returns:	(list): A (y <height>, x <width>) coordinate pair.
	"""
	return (randint(0, board_height-1), randint(0, board_width-1))


def get_symbol(symbol_name: str):
	if symbol_name == "mine":
		return "*"

	if symbol_name == "unflipped":
		return "-"

	if symbol_name == "empty":
		return " "


def generate_new_board():
	## 	Board
	board_dimensions = get_setting("board_dimensions")
	board = np.zeros(board_dimensions)


	##	Mines
	num_mines = get_setting("num_mines")
	n = 0
	while n < num_mines:
		rcs = random_coordinates(board_dimensions[0], board_dimensions[1])

		## Handle duplicates
		if board[rcs] == get_symbol("mine"):
			n = n+1 # Run one more time to try again
			continue

		board[rcs] = -1

		## Adjacents
		# TODO: Don't repeat yourself!
		###	Row above mine
		try:
			board[rcs[0]-1, rcs[1]-1] = board[rcs[0]-1, rcs[1]-1] + 1
		except IndexError:
			pass
		try:
			board[rcs[0]-1, rcs[1]]   = board[rcs[0]-1, rcs[1]]   + 1
		except IndexError:
			pass
		try:
			board[rcs[0]-1, rcs[1]+1] = board[rcs[0]-1, rcs[1]+1] + 1
		except IndexError:
			pass
		###	Same row as mine
		try:
			board[rcs[0], rcs[1]-1]   = board[rcs[0], rcs[1]-1]   + 1
		except IndexError:
			pass
		try:
			board[rcs[0], rcs[1]+1]   = board[rcs[0], rcs[1]+1]   + 1
		except IndexError:
			pass
		###	Row below mine
		try:
			board[rcs[0]+1, rcs[1]-1] = board[rcs[0]+1, rcs[1]-1] + 1
		except IndexError:
			pass
		try:
			board[rcs[0]+1, rcs[1]]   = board[rcs[0]+1, rcs[1]]   + 1
		except IndexError:
			pass
		try:
			board[rcs[0]+1, rcs[1]+1] = board[rcs[0]+1, rcs[1]+1] + 1
		except IndexError:
			pass

		# Update iterator
		n = n+1

	return board

def generate_new_mask(board):
	##	Mask
	mask = np.full(board.shape, get_symbol("unflipped"))
	return mask

def print_board(mask):
	# Column header
	cols = mask.shape[1]
	c = 1
	print("    ", end='') # Space for row headers
	while c <= cols:
		print ("   " + str(c) + "   ", end='')
		c = c + 1
	print()
	r = 1
	for y in mask:
		print(str(r) + "   ", end='')
		for x in y:
			print("   " + x + "   ", end='')
		print("\n")

		r = r + 1

def is_valid_command_code(input: str):
	if input == 'q':
		return True

	return False

def is_valid_coordinate(input: str):
	inp = input.split(',')

	if len(inp) != 2:
		raise ValueError("Invalid coordinates. Requires 2 comma separated values.")

	if int(inp[0]) > get_setting("board_dimensions")[0]:
		raise ValueError("Invalid y (vertical) coordinate. Not on board.")

	if int(inp[1]) > get_setting("board_dimensions")[1]:
		raise ValueError("Invalid x (horizontal) coordinate. Not on board.")

	return True


# Generate board
board = generate_new_board()
mask = generate_new_mask(board)

# Loop
while True:
	# Show the board
	print_board(mask)

	##	Get user input
	###		Prompt
	ui = input("Enter cell coordinates in 'y,x' format or 'q' to quit: ")

	###		Validate
	if not is_valid_command_code(ui):
		try:
			is_valid_coordinate(ui)
		except ValueError:
			print("Invalid coordinates or command. Please try again.")
			continue


	##	Break loop to quit
	if ui == 'q':
		break

	## Uncover mask
	cs = ui.split(",")
	cs = [int(c)-1 for c in cs] # Reconcile 1 indexed user input with 0 indexed arrays
	you_lose = False
	b_cell = board[cs[0], cs[1]]
	if b_cell == -1: # MINE!
		you_lose = True
		mask[cs[0], cs[1]] = get_symbol("mine")

	elif b_cell == 0: # Nothing
		mask[cs[0], cs[1]] = get_symbol("empty")

	else:
		mask[cs[0], cs[1]] = b_cell

	## Status report / reset
	if you_lose:
		print_board(mask)
		input("YOU LOST! Press any key to start a new game.")
		board = generate_new_board()
		mask = generate_new_mask(board)