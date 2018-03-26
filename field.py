#/usr/bin/python3

class Field:
	def __init__(self, width, height):
		self.fields = [[[False] * width] * height] * 3
		# dick below
		# self.fields = [[[True] * 10] * 10, [[True] * 10] * 10]

	def set_cell(self, x, y):
		self.fields[0][y][x] = True

	def process_field(self):
		new_field = self.fields[0][:]
		for y in self.fields[0]:
			for x in self.fields[0][x]:
				new_field[y][x] = process_cell(x, y)

		self.fields = new_field + self:fields[1:]

	def clean(self):
		for i in self.fields[0]:
			for j in self.fields[0][i]:
				self.fields[0][i][j] = False

	def process_cell(x, y):
		neighbours = count_neighbours(x, y)

		if self.fields[0][x][y] and (neighbours == 2 or neighbours == 3):
			return True
		elif neighbours == 3:
			return True
		return False

	def count_neighbours(self, x, y):
		count = 0
		if self.fields[0][x + 1][y]:
			count += 1
		if self.fields[0][x - 1][y]:
			count += 1
		if self.fields[0][x + 1][y + 1]:
			count += 1
		if self.fields[0][x + 1][y - 1]:
			count += 1
		if self.fields[0][x][y + 1]:
			count += 1
		if self.fields[0][x][y - 1]:
			count += 1
		if self.fields[0][x - 1][y - 1]:
			count += 1
		if self.fields[0][x - 1][y + 1]:
			count += 1

	# TODO: Exception handling - нужно остаться на той же строчке

		return count

	def field_similarity(self):
		if self.fields[0] == self.fields[1]:
			return True
		if self.fields[0] == self.fields[2]:
			return True
		#TODO: Make it better

def main():



if __name__ == "__main__":
	main()