#/usr/bin/python3

import tkinter as tk
import threading as th
from time import sleep

class Drawer(th.Thread):
	def __init__(self, window, delay):
		th.Thread.__init__(self)
		self.condition = True
		self.window = window
		self.delay = delay

	def run(self):
		print("Thread started")
		while self.condition:
			self.condition = self.window.update_canvas()
			sleep(self.delay)
		print("Thread exited")

class Window:
	# set 800x600 for 40x30 rectangles
	# set 60x60 for 3x3 rectangles
	def __init__(self, width=800, height=600):
		self.field = None
		self.root = tk.Tk()
		self.width = width
		self.height = height
		self.cell_size = 20
		self.canvas, self.cells = self.configure_window()
		self.cells_params = (self.width // self.cell_size, self.height // self.cell_size)
		self.thread = None

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
		btn_stop = tk.Button(frame, text='Stop', command=self.stop)

		frame.pack(side='bottom')
		btn_start.pack(side='left')
		btn_clear.pack(side='right')
		btn_stop.pack(side='right')

		return canvas, cells

	def change_cell_state(self, event):
		x, y = event.x, event.y
		# print("{}:{} - coords".format(x, y))
		id_x = x // self.cell_size
		id_y = y // self.cell_size
		ratio = self.width // self.cell_size
		# print("{}:{} - indexes".format(id_x, id_y))
		cell = self.cells[id_x + ratio * id_y]

		self.field.set_cell(id_x, id_y)
		if event.widget.itemcget(cell, 'fill') == 'gray':
			event.widget.itemconfig(cell, fill='white')
		else:
			event.widget.itemconfig(cell, fill='gray')

	def clear_field(self):
		if self.thread:
			self.thread.condition = False
		for cell in self.cells:
			self.canvas.itemconfig(cell, fill='white')
		self.field.clean()

	def start(self, f):
		self.field = f
		self.root.mainloop()

	def stop(self):
		if self.thread:
			self.thread.condition = False

	def start_game(self):
		self.update_canvas()
		self.start_thread(0.2)

	def start_thread(self, delay):
		sleep(0.1)
		self.thread = Drawer(self, delay)
		self.thread.setDaemon(True)
		self.thread.start()
		

	def canvas_to_field(self):
		# mistake
		field = [[False for x in range(self.cells_params[0])] for y in range(self.cells_params[1])]
		for i in range(len(self.cells)):
			if self.canvas.itemcget(self.cells[i], 'fill') == 'gray':
				field[i // self.cells_params[0]][i % self.cells_params[0]] = True

		return field

	def update_canvas(self):
		field = self.canvas_to_field()
		new_field, condition = self.field.process_field(field)
		self.update_cells(new_field)

		return condition

	def update_cells(self, field):
		for i in range(len(field)):
			for j in range(len(field[0])):
				index = i + self.cells_params[0] * j
				if field[i][j]:	
					self.canvas.itemconfig(self.cells[index], fill='gray')
				else:
					self.canvas.itemconfig(self.cells[index], fill='white')

def main():
	w = Window()

if __name__ == '__main__':
	main()