"""This file implements a very basic console version of the rock, paper
scissors game."""

from random import randint

def valid_user_input(ui: str) -> bool:
	"""Determines if the passed string is a valid RPS choice."""
	if ui == "rock" or ui == "paper" or ui == "scissors":
		return True

	return False

def left_beats_right(left: str, right: str) -> bool:
	"""Determines if left choice beats right choice in RPS."""
	beats_map = {
		"rock": "scissors",
		"paper": "rock",
		"scissors": "paper"
	}

	if beats_map[left] == right:
		return True

	return False

def random_rps_pick():
	"""Returns a random value of rock, paper, or scissors."""
	rps_set = ("rock", "paper", "scissors")
	i = randint(0, 2)

	return rps_set[i]


while True:
	ui = input('Enter a choice of "rock", "paper", or "scissors", or "q" to quit:  ')

	if ui == 'q':
		break

	if valid_user_input(ui):
		pc_pick = random_rps_pick()
		print("Computer Picked: " + pc_pick)

		if left_beats_right(ui, pc_pick):
			print("YOU WIN! Have a cookie.")
		elif left_beats_right(pc_pick, ui):
			print("OH NO! You lost to a stinking computer! No cookie for you.")
		else:
			print("Nobody won or lost. That was anticlimactic.")

	else:
		print("You didn't read the instructions! That's not a valid choice!")

	print()