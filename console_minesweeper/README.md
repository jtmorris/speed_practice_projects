# Console Minesweeper
This is a small console minesweeper game. It generates a 9x9 grid with
2 mines. User inputs coordinates of individual cells to check.

<p align="center">
	<img src="resources/console_minesweeper_1.png">
</p>

The goal was to develop this quickly. I would normally have implemented
customizable board dimensions; however, the adaptive spacing in the grid
display would have taken time to implement correctly and test that I did
not have in my self-imposed time constraints. Nonetheless, the code is
abstracted sufficiently and basic foundations for variable board length
are implemented such that complete implementation should be relatively
simple, should it be desired.

## Requires
Python 3.5+

## Usage
```
$ python console_minesweeper.py
```

## Needed Improvements
The goal of this project was development speed. I'm drilling my
programming speed. As such, my goal was to get a functioning script
without glaringly poor programming practice or carelessly engineered
difficulty of future modification. Not to make the tightest possible
design possible. With more time, I would make the following changes:

### Customizable Board Dimensions
As described above, variable board dimensions beyond single digit widths
and heights would require adaptive spacing and padding of cells. The
code is structured in a manner where that is relatively simple to
implement; however, doing so would have required time.

### Colors, Symbols, and Formatting
Some minimal console colors would be nice. For example, a red mine symbol.
Additionally, some better formatting and/or non-continuous console scroll
would look better. Once again, simple enough, but time consuming.

### More Elegant Adjacent Cell Number Calculation
The method for finding indicators of cells adjacent to mines is far too
kludgy and repetitive for my taste. There is almost certainly a better
way to find that.

### Documentation
Several functions lack documentation. I was pushing my allotted time,
so I omitted some documentation in favor of getting a fully functional
game.