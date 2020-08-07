# Sudoku Solver
## Description
This is a sudoku solver using python for the solving algorithm. It also prints out the solved board, as well as the board used as input to the command line.

It can solve sudoku through logic alone, which it will try first. The logic used is basic logic for solving the board. Afterwards, it will attempt to solve it through guessing, however, it will guess through the square with the lowest number of possibilities and save it's state in case it's wrong.

It can also solve all solutions, if the sudoku board just happens to have multiple solutions.

Requires Python 3 to be installed.
## Instructions

### Input
The input is a csv file with each space representing the number in that square, where an empty sudoku square is an empty csv space. The first row of sudoku board is represented by the first row of the csv file.
### Command
Usage: py Sudoku_Solve -f (input_file)