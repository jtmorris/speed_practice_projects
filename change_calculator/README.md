# Console Change Calculator
This is a small console application which takes a user input number of
cents and calculates the most efficient change breakdown for that value.

## Requires
Python 3.5+

## Usage
```
python change_calculator.py
Type 'q' to quit.

Enter a dollar value in cents: 33

Quarters: 1
Nickels: 1
Pennies: 3


Type 'q' to quit.

Enter a dollar value in cents: q
```

## Needed Improvements
The goal of this project was development speed. I'm drilling my
programming speed. As such, my goal was to get a functioning script
without glaringly poor programming practice or carelessly engineered
difficulty of future modification. Not to make the tightest possible
design possible. With more time, I would make the following changes:

### Toggle Change Usage
Loosely incorporated in the code is the ability to turn on and off
specific coins. For example, by changing a single boolean value, the
script will support half dollar coins. By default, that is disabled.
By default, if more than 100 cents is specified, dollars are specified.
All that is adjustable with simple code tweaks.

Ideally, that would be console command parameterized and/or settings file
defined. Or even an in-program settings alteration method. Remove the
need to edit source code. This could easily be implemented with console
arguments and Python's [argparse](https://docs.python.org/3/library/argparse.html_)
library.

### Testing
Some basic doc, unit, and/or functionality testing is called for. Some light
doctesting is included. To implement testing efficiently, nearly
everything inside the main user prompt loop should be its own function.
Namely, each step of the change calculation logic should be its own
function. Each function could then have unit testing, validating the
logic. Or, for simplicity, each function could have built-in doctesting,
as each function would be exceedingly simple.

### Output Formatting
At minimum, the number of coins in the output should stack vertically. That
requires padding some space (guaranteed, but requires overhead and code),
using tabs (easiest, but tabs can be finnicky and unreliable), or some
other method used in conjunction to obtain other formatting desires (e.g.
a pretty table).