# Pi Calculator
This is a small console application which calculates pi to a specified
number of decimal places using a [Nilakantha series](https://en.wikipedia.org/wiki/Pi#Infinite_series)
expansion.

The goal was to develop this quickly. It did not go as quickly as I would
have liked. The basic structure came together, but I spent far too long
battling math with floats, string formatting floats, and debugging. It
was a good exercise, but did not help me achieve my goal of SPEED!

## Requires
Python 3.5+

## Usage
```
$ python pi_calculator.py --decimals 25


Iteration #: 170998
Last Pi: 3.141592653589793
Cur Pi: 3.141592653589793
Delta: 9.999841169300E-17
Delta Threshold: 1e-16
Exec Time: 1.0024685859680176 seconds

Result: 3.141592653589793
```

## Needed Improvements
The goal of this project was development speed. I'm drilling my
programming speed. As such, my goal was to get a functioning script
without glaringly poor programming practice or carelessly engineered
difficulty of future modification. Not to make the tightest possible
design possible. With more time, I would make the following changes:

### Performance Optimization
The Nilakantha series method is slowly converging, and requires many
thousands of loop iterations to achieve any major decimal accuracy. If
continuing to use Nilakantha series, ruthlessly murdering inefficiency
in the loop would pay dividends in calculation speed.

Additionally, multithreading may help given the large numbers and major
division going on.