class Sudoku_Square:
	
	# Instantiate square
	def __init__(self, value):
		if value == 0:
			self.value = 0
			self.possible_values = list(range(1,10))
		else:
			self.value = value
			self.possible_values = [value]
	
	# Remove value from possible_values list and set value if only one possible value exists.
	def remove_possible_value(self, num):
		self.possible_values.remove(num)
		if len(self.possible_values) == 1:
			self.set_value(self.possible_values[0])
			return True
		return False

	# Set value and replace possible_values
	def set_value(self, num):
		self.value = num
		self.possible_values.clear()
		self.possible_values.append(num)
		
	# Get value of square
	def get_value(self):
		return self.value
		
	# Get possible_values of square
	def get_possible_values(self):
		return self.possible_values