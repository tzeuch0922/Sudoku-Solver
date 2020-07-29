from Sudoku_Square import Sudoku_Square
import sys

class Sudoku_Board:
	
	# Instantiate board
	def __init__(self, board):
	
		# Check to see if board is correct length and exits with error, if not.
		if len(board) != 81:
			print("Board length error:")
			print("Board should be 81 in length, but it is currently " + str(len(board)) + " in length.")
			sys.exit()
		
		self.board = []
		
		for val in board:
			if val <= 9:
				self.board.append(Sudoku_Square(val))
			else:
				print("Board element error:")
				print("Board values can only be from 0 to 9. Current board value is " + str(val) + ".")
		
	# Print sudoku board
	def print_board(self):
		for i in range(0,9):
			if i % 3 == 0:
				print("_________________________")
			list = [self.board[j].get_value() for j in range(i*9, (i+1)*9)]
			formatted_string = "| {} {} {} | {} {} {} | {} {} {} |".format(*list)
			print(formatted_string.replace('0', ' '))
		print("_________________________")
	
	# Return list of sudoku squares in row affecting square
	def squares_in_row(self, x, y):
		return [self.board[i] for i in range(y * 9, (y * 9) + 9) if i % 9 != x]
		
	# Return list of sudoku squares in column affecting square	
	def squares_in_col(self, x, y):
		return [self.board[i] for i in range(x, 81, 9) if i // 9 != y]
		
	# Return list of sudoku squares in square affecting square
	def squares_in_square(self, x, y):
		return [self.board[i] for i in range((y // 3 * 3) * 9, (y //3 * 3 * 9) + 27) if((i % 9) // 3 == x // 3 and i != (y * 9) + x)]
		
	# Return sudoku square
	def get_square(self, x, y):
		return self.board[(y * 9) + x]
	
	# Function to check to see if current board is legal
	def is_legal(self):
		for x in range(0, 9):
			for y in range(0, 9):
				if len(self.get_square(x, y).get_possible_values()) == 0:
					#print("No possible values at: (" + str(x) + " ," + str(y) + " )")
					return False
				for square in self.squares_in_row(x, y):
					if square.get_value() != 0 and square.get_value() == self.get_square(x, y).get_value():
						#print("Value identical in row for value at: (" + str(x) + " ," + str(y) + " )")
						return False
				for square in self.squares_in_col(x, y):
					if square.get_value() != 0 and square.get_value() == self.get_square(x, y).get_value():
						#print("Value identical in col for value at: (" + str(x) + " ," + str(y) + " )")
						return False
				for square in self.squares_in_square(x, y):
					if square.get_value() != 0 and square.get_value() == self.get_square(x, y).get_value():
						#print("Value identical in square for value at: (" + str(x) + " ," + str(y) + " )")
						return False
		return True
	
	# Function to check to see if current board is finished
	def is_finished(self):
		if not self.is_legal():
			return -1
		for x in range(0, 9):
			for y in range(0, 9):
				if self.get_square(x, y).get_value() == 0:
					return 0
		return 1

# Test functionality so far
if __name__ == "__main__":
	arr = []
	for i in range(0, 81):
		if (i // 9) % 2 == 0:
			arr.append(i % 9)
		else:
			arr.append((i % 9) + 1)
	board = Sudoku_Board(arr)
	board.print_board()