from Sudoku_Board import Sudoku_Board
import argparse
import csv
import copy

# Return csv items in a list
def read_csv_to_list(file_name):
	list = []
	with open(file_name, newline = '') as csvfile:
		reader = csv.reader(csvfile, quotechar = '|')
		for row in reader:
			for item in row:
				list.append(item)
	list = [0 if i == '' else i for i in list]
	list = [int(i) for i in list]
	return list
	
# Start solving process by marking up board
def mark_possible_values(problem):
	values_marked = [False for i in range(0, 81)]
	no_changes = False
	while not no_changes:
		no_changes = True
		for x in range(0, 9):
			for y in range(0, 9):
				if problem.get_square(x, y).get_value() != 0 and not values_marked[(y * 9) + x]:
					no_changes = False
					remove_values(problem, x, y)
					values_marked[(y * 9) + x] = True
	
# Continue solving process by finding values that can only be in one place	
def solve_lone_values(problem):
	no_changes = False
	while not no_changes:
		no_changes = True
		for x in range(0, 9):
			for y in range(0, 9):
				if problem.get_square(x, y).get_value() == 0:
					row = problem.squares_in_row(x, y)
					col = problem.squares_in_col(x, y)
					area = problem.squares_in_square(x, y)
					for val in problem.get_square(x, y).get_possible_values():
						lone_value = True
						for square in row:
							if val in square.get_possible_values():
								lone_value = False
								break
						if lone_value:
							problem.get_square(x, y).set_value(val)
							remove_values(problem, x, y)
							no_changes = False
							break	
						for square in col:
							if val in square.get_possible_values():
								lone_value = False
								break
						if lone_value:
							problem.get_square(x, y).set_value(val)
							remove_values(problem, x, y)
							no_changes = False
							break
						for square in area:
							if val in square.get_possible_values():
								lone_value = False
								break
						if lone_value:
							problem.get_square(x, y).set_value(val)
							remove_values(problem, x, y)
							no_changes = False
							break

# Function to remove all values that become impossible.
def remove_values(problem, x, y):
		square_value = problem.get_square(x, y).get_value()
		row = problem.squares_in_row(x, y)
		col = problem.squares_in_col(x, y)
		area = problem.squares_in_square(x, y)
		for square in row:
			if square.get_value() == 0 and square_value in square.get_possible_values():
				square.remove_possible_value(square_value)
		for square in col:
			if square.get_value() == 0 and square_value in square.get_possible_values():
				square.remove_possible_value(square_value)
		for square in area:
			if square.get_value() == 0 and square_value in square.get_possible_values():
				square.remove_possible_value(square_value)
				
# Function to find square with lowest number of possibilities.
def find_simplest_square(problem):
	x_index = 0
	y_index = 0
	smallest_len = 9
	for x in range(0, 9):
		for y in range(0, 9):
			if problem.get_square(x, y).get_value() == 0 and len(problem.get_square(x, y).get_possible_values()) < smallest_len:
				x_index = x
				y_index = y
				smallest_len = len(problem.get_square(x, y).get_possible_values())
	return [x_index, y_index]
				
if __name__ == "__main__":
	# Command-line arguments
	parser = argparse.ArgumentParser("Solves a sudoku problem indicated in a csv file.")
	parser.add_argument("-f", "--file_name", action = "store", help = "Name of csv file for input.", required = True)
	options = parser.parse_args()
	
	board_save_states = []
	board_solutions = []
	file_name = str(options.file_name)
	Sudoku_Problem = Sudoku_Board(read_csv_to_list(file_name))
	print("Starting Board:")
	Sudoku_Problem.print_board()
	while True:
		mark_possible_values(Sudoku_Problem)
		solve_lone_values(Sudoku_Problem)
		mark_possible_values(Sudoku_Problem)
		finished = Sudoku_Problem.is_finished()
		if finished == 1:
			temp_board = copy.deepcopy(Sudoku_Problem)
			board_solutions.append(temp_board)
			if len(board_save_states) == 0:
				break
			else:
				Sudoku_Problem = board_save_states.pop()
		elif finished == 0:
			index_arr = find_simplest_square(Sudoku_Problem)
			x_index = index_arr[0]
			y_index = index_arr[1]
			for value in Sudoku_Problem.get_square(x_index, y_index).get_possible_values():
				temp_board = copy.deepcopy(Sudoku_Problem)
				temp_board.get_square(x_index, y_index).set_value(value)
				board_save_states.append(temp_board)
			Sudoku_Problem = board_save_states.pop()
		elif finished == -1:
			if len(board_save_states) != 0:
				Sudoku_Problem = board_save_states.pop()
			else:
				break
	if len(board_solutions) == 0:
		print("No solutions")
	elif len(board_solutions) == 1:
		print("Solution:")
		board_solutions[0].print_board()
	else:
		for i in range(0, len(board_solutions)):
			print("Solution " + str(i+1) + ":")
			board_solutions[i].print_board()