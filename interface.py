#/usr/bin/python3

import tkinter as tk

class Window:
	def __init__(self, width=800, height=600):
		self.field = None
		self.root = tk.Tk()
		self.width = width
		self.height = height
		self.cell_size = 20
		self.canvas, self.cells = self.configure_window()
		self.cells_params = (self.width // self.cell_size, self.height // self.cell_size) 

	def configure_window(self):
		geometry = '{}x{}'.format(self.width, self.height+100)
		self.root.geometry(geometry)

		cells = []
		canvas = tk.Canvas(self.root, width=self.width, height=self.height)
		for i in range(self.height // self.cell_size):
			for j in range(self.width // self.cell_size):
				cells.append(canvas.create_rectangle(j * self.cell_size, i * self.cell_size, (j+1) * self.cell_size, (i+1) * self.cell_size, fill='white'))

		canvas.pack(fill=tk.BOTH)

		canvas.bind('<Button 1>', self.change_cell_state)
		canvas.bind('<B1-Motion>', self.change_cell_state)

		frame = tk.Frame(self.root)

		btn_start = tk.Button(frame, text='Start', command=self.start_game)
		btn_clear = tk.Button(frame, text='Clear', command=self.clear_field)

		frame.pack(side='bottom')
		btn_start.pack(side='left')
		btn_clear.pack(side='right')

		return canvas, cells

	def change_cell_state(self, event):
		x, y = event.x, event.y
		print("{}:{} - coords".format(x, y))
		id_x = x // self.cell_size
		id_y = y // self.cell_size
		ratio = self.width // self.cell_size
		print("{}:{} - indexes".format(id_x, id_y))
		cell = self.cells[id_x + ratio * id_y]

		self.field.set_cell(id_x, id_y)
		event.widget.itemconfig(cell, fill='gray')

	def start_game(self):
		pass

	def clear_field(self):
		for cell in self.cells:
			self.canvas.itemconfig(cell, fill='white')
			# TODO: change field also
		self.field.clean()

	def start(self, f):
		self.field = f
		self.root.mainloop()

def main():
	w = Window()

if __name__ == '__main__':
	main()