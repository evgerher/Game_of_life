#/usr/bin/python3

class Field:
	def __init__(self, width, height):
		self.fields = [[[False for y in range(height)] for x in range(width)] for z in range(3)]
		self.x_border = width
		self.y_border = height

	def set_cell(self, x, y):
		self.fields[0][x][y] = not self.fields[0][x][y]
		# print('After updated field:\n{}'.format(self.fields[0]))

	def process_field(self, field=None):
		if field:
			# print("Field from app----\n")
			# self.print_field(field)
			for i in range(len(field)):
				for j in range(len(field[i])):
					self.fields[0][j][i] = field[i][j]

		# self.print_field()
		new_field = [[False for y in range(self.y_border)] for x in range(self.x_border)]
		for x in range(len(self.fields[0])):
			for y in range(len(self.fields[0][x])):
				new_field[x][y] = self.process_cell(x, y)


		# self.print_field(new_field)
		self.fields = [new_field] + self.fields[0:-1]

		condition = self.check_condition()
		
		# print ('Result field after processing...\n{}'.format(self.fields[0]))
		return self.fields[0], condition

	# def print_field(self):
	# 	for j in range(len(self.fields[0][0])):
	# 		for i in range(len(self.fields[0])):
	# 			print(1 if self.fields[0][i][j] else 0, end='')
	# 		print('')
	# 	print(self.x_border, self.y_border)

	def print_field(self, field=None):
		if field is None:
			field = self.fields[0]
		for i in range(len(field)):
			for j in range(len(field[i])):
				print(1 if field[i][j] else 0, end='')
			print('')
		print(self.x_border, self.y_border)

	def check_condition(self):
		return not self.field_similarity()

	def clean(self):
		for i in range(len(self.fields[0])):
			for j in range(len(self.fields[0][i])):
				self.fields[0][i][j] = False

	def process_cell(self, x, y):
		neighbours = self.count_neighbours(x, y)

		if self.fields[0][x][y] and (neighbours == 2 or neighbours == 3):
			return True
		elif neighbours == 3:
			return True
		return False

	def count_neighbours(self, x, y):
		right_x = (x + 1) % self.x_border
		right_y = (y + 1) % self.y_border
		left_x = (x - 1) if (x - 1) >= 0 else self.x_border - 1
		left_y = (y - 1) if (y - 1) >= 0 else self.y_border - 1

		# print ('RIGHT: 	{} and {}'.format(right_x, right_y))
		# print ('LEFT: 	{} and {}'.format(left_x, left_y))
		# print ('x&y: 		{} and {}'.format(x, y))


		# if (y, x) == (4, 2):
		# 	print (left_y, left_x)
		# 	print (left_y, x)
		# 	print (left_y, left_x)

		# count = 0
		# if self.fields[0][y][right_x]:
		# 	count += 1
		# if self.fields[0][y][left_x]:
		# 	count += 1
		# if self.fields[0][right_y][right_x]:
		# 	count += 1
		# if self.fields[0][right_y][left_x]:
		# 	count += 1
		# if self.fields[0][y][right_x]:
		# 	count += 1
		# if self.fields[0][y][left_x]:
		# 	count += 1
		# if self.fields[0][left_y][left_x]:
		# 	count += 1
		# if self.fields[0][left_y][right_x]:
		# 	count += 1
		# if (x, y) == (1,1):
		# 	self.print_field()

		count = 0
		if self.fields[0][right_x][y]:
			# print('neighbour [right_x][y]')
			count += 1
		if self.fields[0][left_x][y]:
			# print('neighbour [left_x][y]')
			count += 1
		if self.fields[0][right_x][right_y]:
			# print('neighbour [right_x][right_y]')
			count += 1
		if self.fields[0][left_x][right_y]:
			# print('neighbour [left_x][right_y]')
			count += 1
		if self.fields[0][x][right_y]:
			# print('neighbour [x][right_y]')
			count += 1
		if self.fields[0][x][left_y]:
			# print('neighbour [x][left_y]')
			count += 1
		if self.fields[0][left_x][left_y]:
			# print('neighbour [left_x][left_y]')
			count += 1
		if self.fields[0][right_x][left_y]:
			# print('neighbour [right_x][left_y]')
			count += 1


		# print('Cell [{}:{}] has {} neighbours...\n'.format(x, y, count))

		return count

	def field_similarity(self):
		# print("LEN OF FIELDS {}".format(len(self.fields)))
		if self.fields[0] == self.fields[1]:
			return True
		if self.fields[0] == self.fields[2]:
			return True
		#TODO: Make it better
		return False

def main():
	print ("hell")


if __name__ == "__main__":
	main()