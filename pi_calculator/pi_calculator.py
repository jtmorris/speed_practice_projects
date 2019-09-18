import argparse
import time
import decimal

def format_decimal(num: float, decimal_places: int):
	"""Formats float as a string with number of decimal places."""
	return format(num, '.' + str(decimal_places) + 'f')

def nilakantha_status_report(iterations: int, last_pi, cur_pi, delta,
                             delta_thresh, exec_time, decimal_limit):
	"""Returns a readable status report with the specified data."""

	retstr = "Iteration #: " + str(iterations) + "\n" \
		"Last Pi: " + format_decimal(last_pi, decimal_limit) + "\n" \
		"Cur Pi: " + format_decimal(cur_pi, decimal_limit) + "\n" \
		"Delta: " + str(delta) + "\n" \
		"Delta Threshold: " + str(delta_thresh) + "\n" \
		"Exec Time: " + str(exec_time) + " seconds\n"

	return retstr

def nilakantha_series(decimal_limit: int=100, iteration_limit: int=None,
                      print_continuous_status_report: bool=False,
				  print_end_status_report: bool=True):
	"""Use the Nilakantha series method to calculate pi.

	Uses a Nilakantha series expansion to calculate pi until the
	specified number of decimals is reached. Nilakantha should converge
	on the accuracy quickly; however, bear in mind greater accuracy
	requires additional processing power and if the number is insanely
	large, may yield memory usage problems.

	Parameters:
		decimal_limit (int): The number of decimals to calculate to.
		iteration_limit (int): The maximum number of loop iterations
		                       to execute. Whichever limit is reached
						   first will end the loop.
		print_continuous_status_report (bool): Output status report on
		                                       each loop iteration.
									    This is very slow!
									    Defaults to False.
		print_end_status_report (bool): Output status report at end of
		                                loop. Defaults to True.

	Returns:
		(float): A signed floating point decimal containing pi to
		the correct digit.
	"""
	decimal.getcontext().prec = decimal_limit*2 # *2 to ensure more accuracy

	i = 1
	d1 = 2	# First number in denominator series.
	sign_coeff = 1	# A coefficient to alter between addition and subtraction
	pi = decimal.Decimal(3)
	last_pi = pi
	stop_after = None
	start_time = time.time()
	while True:
		# Update last_pi
		last_pi = pi

		# Determine denominators
		d2 = d1 + 1
		d3 = d2 + 1

		# Expand series
		den = decimal.Decimal(d1*d2*d3)
		num = decimal.Decimal(4)
		pi = pi + sign_coeff*(num/den)

		# Check if this is signaled as our last run
		if type(stop_after) == int:
			if stop_after <= 1:
				break
			else:
				stop_after = stop_after - 1

		# Check limits
		#	Iteration limit
		if iteration_limit and i >= iteration_limit:
			print("Iteration limit reached.")
			break

		#	Decimal limit
		#		Decimal limit will be met by ensuring lack of variance
		# 		beyond the requested decimal limt by 1 decimal place.
		#		This method can become costly at very high precisions.
		if decimal_limit:
			delta = abs(pi - last_pi)
			delta_thresh = 10**(-1*(decimal_limit+1))
			if delta < delta_thresh:
				break

		# Print status report
		if print_continuous_status_report:
			print("\n" + nilakantha_status_report(i, last_pi, pi, delta,
				delta_thresh, time.time() - start_time, decimal_limit))


		# Update iterators
		i = i + 1

		# Update denominators and signs for next iteration
		d1 = d3
		sign_coeff = sign_coeff * -1

	if print_end_status_report:
			print("\n" + nilakantha_status_report(i, last_pi, pi, delta,
				delta_thresh, time.time() - start_time, decimal_limit))
	return pi



AP = argparse.ArgumentParser()
AP.add_argument("-d", "--decimals",
                help="An integer number of decimal places to hold accuracy.",
			 type=int, default=10)
AP.add_argument("-i", "--iterations",
                help="An integer number of iterations to limit execution to.",
			 type=int, default=None)

args = vars(AP.parse_args())

pi = nilakantha_series(args.get("decimals", 10000), args.get("iterations", None), False)

print("Result: " + format_decimal(pi, args.get("decimals", 10)))