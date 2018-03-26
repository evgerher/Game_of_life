#/usr/bin/python3

class Field:
	def __init__(self, width, height):
		self.fields = [[[False for x in range(width)] for y in range(height)] for z in range(3)]
		self.x_border = width
		self.y_border = height

	def set_cell(self, x, y):
		self.fields[0][y][x] = True
		# print('After updated field:\n{}'.format(self.fields[0]))

	def process_field(self, field=None):
		if field:
			# print ('Field came from app :\n {}'.format(field))
			for i in range(len(field)):
				for j in range(len(field[i])):
					self.fields[0][i][j] = field[i][j]

		new_field = self.fields[0][:]
		for y in range(len(self.fields[0])):
			for x in range(len(self.fields[0][y])):
				new_field[y][x] = self.process_cell(x, y)

		self.fields = [new_field] + self.fields[1:]

		condition = self.check_condition()
		
		# print ('Result field after processing...\n{}'.format(self.fields[0]))
		return self.fields[0], condition

	def check_condition(self):
		return not self.field_similarity()

	def clean(self):
		for i in range(len(self.fields[0])):
			for j in range(len(self.fields[0][i])):
				self.fields[0][i][j] = False

	def process_cell(self, x, y):
		neighbours = self.count_neighbours(x, y)

		if self.fields[0][y][x] and (neighbours == 2 or neighbours == 3):
			return True
		elif neighbours == 3:
			return True
		return False

	def count_neighbours(self, x, y):
		right_x = (x + 1) % self.x_border
		right_y = (y + 1) % self.y_border
		left_x = (x - 1) if (x - 1) > 0 else self.x_border - 1
		left_y = (y - 1) if (y - 1) > 0 else self.y_border - 1

		# print('On count : {}'.format(self.fields[0]))

		count = 0
		if self.fields[0][y][right_x]:
			count += 1
		if self.fields[0][y][left_x]:
			count += 1
		if self.fields[0][right_y][right_x]:
			count += 1
		if self.fields[0][left_y][right_x]:
			count += 1
		if self.fields[0][right_y][x]:
			count += 1
		if self.fields[0][left_y][x]:
			count += 1
		if self.fields[0][left_y][left_x]:
			count += 1
		if self.fields[0][right_y][left_x]:
			count += 1

		# print('Cell [{}:{}] has {} neighbours...'.format(x, y, count))

		return count

	def field_similarity(self):
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