#/usr/bin/python3

"""
Class Field
The logic unit of the Game of Life
"""
class Field:
	'''
	Constructor accepts amount of items in a row and in a column
	'''
	def __init__(self, width, height):
		self.fields = [[[False for y in range(height)] for x in range(width)] for z in range(3)]
		self.x_border = width
		self.y_border = height

	'''
	set_cell method
	Alters a cell of a given position
	'''
	def set_cell(self, x, y):
		self.fields[0][x][y] = not self.fields[0][x][y]

	'''
	process_field method
	0) if new field - saves it
	1) Processes the first field and constructs a new one
	2) Checks the final condition
	3) Returns new field and condition
	'''
	def process_field(self, field=None):
		# Accept new field (necessary for Drawer thread)
		if field:
			for i in range(len(field)):
				for j in range(len(field[i])):
					self.fields[0][j][i] = field[i][j]

		# New field initialization
		new_field = [[False for y in range(self.y_border)] for x in range(self.x_border)]
		# Step by step process cells
		for x in range(len(self.fields[0])):
			for y in range(len(self.fields[0][x])):
				new_field[x][y] = self.process_cell(x, y)

		# Remove oldest field
		self.fields = [new_field] + self.fields[0:-1]

		# Final state
		condition = self.check_condition()
		
		return self.fields[0], condition

	'''
	print_field method
	Prints the accepted field and borders of the field
	Useful for debug
	'''
	def print_field(self, field=None):
		if field is None:
			field = self.fields[0]
		for i in range(len(field)):
			for j in range(len(field[i])):
				print(1 if field[i][j] else 0, end='')
			print('')
		print(self.x_border, self.y_border)

	# Returns end condtion
	# Why not self.field_similarity() ?
	# Because field similar - yes
	# End if fields are similar (False state for the interface module)
	def check_condition(self):
		return not self.field_similarity()

	# Clean method
	# Wipes the 2D-array
	def clean(self):
		for i in range(len(self.fields[0])):
			for j in range(len(self.fields[0][i])):
				self.fields[0][i][j] = False

	# process_cell method
	# Returns the state of a cell
	def process_cell(self, x, y):
		neighbours = self.count_neighbours(x, y)

		# Still alive
		if self.fields[0][x][y] and (neighbours == 2 or neighbours == 3):
			return True
		# Born from ashes
		elif neighbours == 3:
			return True
		return False
	
	# count_neighbours method
	# Counts the amount of neighbours around
	def count_neighbours(self, x, y):
		# If the borders of the map - connect it as a torus
		right_x = (x + 1) % self.x_border
		right_y = (y + 1) % self.y_border
		left_x = (x - 1) if (x - 1) >= 0 else self.x_border - 1
		left_y = (y - 1) if (y - 1) >= 0 else self.y_border - 1
		count = 0

		if self.fields[0][right_x][y]:
			count += 1
		if self.fields[0][left_x][y]:
			count += 1
		if self.fields[0][right_x][right_y]:
			count += 1
		if self.fields[0][left_x][right_y]:
			count += 1
		if self.fields[0][x][right_y]:
			count += 1
		if self.fields[0][x][left_y]:
			count += 1
		if self.fields[0][left_x][left_y]:
			count += 1
		if self.fields[0][right_x][left_y]:
			count += 1

		# print('Cell [{}:{}] has {} neighbours...\n'.format(x, y, count))

		return count
	
	# field_similarity method
	# Checks that there are repeating creatures (duration is up to 3)
	def field_similarity(self):
		if self.fields[0] == self.fields[1]:
			return True
		if self.fields[0] == self.fields[2]:
			return True
		return False