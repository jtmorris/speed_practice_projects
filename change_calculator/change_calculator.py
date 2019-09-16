#!/usr/bin/env python
"""
This file is a small console program that takes user input of cents and
calculates the most efficient change breakdown of that value.
"""

def validate_input(cents: int, exceptions_on: bool=True):
	"""Validates user input cents.

	Checks to make sure input is an integer and is a valid cents value.
	If it is, the value is returned. If it isn't, an exception is
	raised and None is returned.

	Parameters:
		cents (int):   The cents input to validate.
		exceptions_on: Whether to raise exceptions on error. Defaults to True.

	Returns:
		(int): The cents input if valid. None if not.

	Exceptions:
		ValueError:
			If value does not pass validation checks.
		TypeError:
			If value is not an integer.

	Examples:
		>>> validate_input(100, False)
		100
		>>> validate_input("100", False)
		>>> validate_input("-1", False)
		>>> validate_input("abcdefg", False)
	"""

	# Checking for integer value should happen during function call,
	# thanks to type hinting. However, just to be absolutely sure, and
	# to facilitate doctesting, check the types here explicitly.
	if not (isinstance(cents, int)):
		if exceptions_on:
			raise TypeError("Cents must be integers.")
		return None

	# Integer must be positive or zero
	if not cents >= 0:
		if exceptions_on:
			raise ValueError("Negative cents values are invalid.")
		return None

	return cents


def output_formatted_report(dollars: int=None, half_dollars: int=None,
                            quarters: int=None, dimes: int=None,
					   nickels: int=None, pennies: int=None):

	print()
	if dollars:
		print("Dollars: " + str(dollars))
	if half_dollars:
		print("Half Dollars: " + str(half_dollars))
	if quarters:
		print("Quarters: " + str(quarters))
	if dimes:
		print("Dimes: " + str(dimes))
	if nickels:
		print("Nickels: " + str(nickels))
	if pennies:
		print("Pennies: " + str(pennies))

	print("\n")


while True:
	print("Type 'q' to quit.\n")
	cents = input("Enter a dollar value in cents: ")

	if cents == 'q':
		break

	# Validate user input
	try:
		cents = int(cents)
		validate_input(cents)
	except (ValueError, TypeError):
		print("Invalid input. Try again.")
		continue


	# Filter change options
	use_dollars      = True
	use_half_dollars = False
	use_quarters     = True
	use_dimes        = True
	use_nickels      = True
	use_pennies      = True


	remaining_cents  = cents
	num_dollars      = None
	num_half_dollars = None
	num_quarters     = None
	num_dimes        = None
	num_nickels      = None
	num_pennies      = None

	# How many whole dollars
	if use_dollars:
		num_dollars = int(cents / 100)
		remaining_cents = remaining_cents - num_dollars*100

	# How many half dollars
	if use_half_dollars:
		num_half_dollars = int(cents / 50)
		remaining_cents = remaining_cents - num_half_dollars*50

	# How many whole quarters
	if use_quarters:
		num_quarters = int(remaining_cents / 25)
		remaining_cents = remaining_cents - num_quarters*25

	# How many whole dimes
	if use_dimes:
		num_dimes = int(remaining_cents / 10)
		remaining_cents = remaining_cents - num_dimes*10

	# How many whole nickels
	if use_nickels:
		num_nickels = int(remaining_cents / 5)
		remaining_cents = remaining_cents - num_nickels*5

	# How many whole nickels
	if use_pennies:
		num_pennies = remaining_cents

	output_formatted_report(num_dollars, num_half_dollars, num_quarters,
	                        num_dimes, num_nickels, num_pennies)