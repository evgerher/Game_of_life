#/usr/bin/python3

import tkinter as tk
import threading as th
from time import sleep

'''
Thread for autoupdating the canvas
Initializes next step and redraws the screen
'''
class Drawer(th.Thread):
	''' 
	window - Window object for calling update_canvas()
	delay - time in seconds till next iteration
	condition - end condition for a thread
	'''
	def __init__(self, window, delay=0.5):
		th.Thread.__init__(self)
		self.condition = True
		self.window = window
		self.delay = delay

	# Initializes a job for a thread
	# until condition will become False the thread will continue its work
	def run(self):
		print("Thread started")
		while self.condition:
			self.condition = self.window.update_canvas()
			sleep(self.delay)
		print("Thread exited")

""" 
Class Window
Collaborates all the GUI components and Field components
Stores GUI processing units and receives updates from Field object
"""
class Window:
	# set 800x600 for 40x30 rectangles
	# set 60x60 for 3x3 rectangles
	def __init__(self, width=800, height=600, cell_size=20, thread_active=True, patterns=None):
		self.field = None # Field object, stores logic and constructs new iteration of the map
		self.root = tk.Tk() # GUI root object
		self.width = width # Width of the screen
		self.height = height # Height of the screen
		self.cell_size = cell_size # size AxA pixels of the rectangles in the canvas
		self.patterns = patterns
		self.canvas, self.cells = self.configure_window() # Init method for GUI
		self.cells_params = (self.width // self.cell_size, self.height // self.cell_size) # Store amount of cells in width and height for later needs
		self.thread = None # Thread for parallel update
		self.thread_active = thread_active

	""" 
	Method configure_window
	Initializes different tools and widgets for the GUI
	Set ups rectangles (cells) and binds buttons 

	Returns `canvas` object and `cells` list
	"""
	def configure_window(self):
		# Set up window size
		geometry = '{}x{}'.format(self.width, self.height+100)
		self.root.geometry(geometry)

		# Initialize canvas
		canvas = tk.Canvas(self.root, width=self.width, height=self.height)

		# Initialize cells
		cells = []
		for i in range(self.height // self.cell_size):
			for j in range(self.width // self.cell_size):
				cells.append(canvas.create_rectangle(j * self.cell_size, i * self.cell_size, (j+1) * self.cell_size, (i+1) * self.cell_size, fill='white'))

		# Hold left mouse press and motion of pressed left button as an update for a cell
		canvas.bind('<Button 1>', self.change_cell_state)
		canvas.bind('<B1-Motion>', self.change_cell_state)

		frame = tk.Frame(self.root)

		# Button inialization
		btn_start = tk.Button(frame, text='Start', command=self.start_game)
		btn_step = tk.Button(frame, text='Step', command=self.update_canvas)
		btn_clear = tk.Button(frame, text='Clear', command=self.clear_field)
		btn_stop = tk.Button(frame, text='Stop', command=self.stop)
		if self.patterns:
			for name in self.patterns.keys():
				btn = tk.Button(frame, text=name, command=self.draw_figure)
				btn.bind('<Button-1>', self.draw_figure)
				btn.pack(side='right')

		# Items packing
		canvas.pack(fill=tk.BOTH)
		frame.pack(side='bottom')
		btn_start.pack(side='left')
		btn_step.pack(side='left')
		btn_stop.pack(side='left')
		btn_clear.pack(side='left')

		return canvas, cells

	""" 
	Method draw_figure
	Supports patterns feature
	Draws a pattern in coordinates provided by pattern dictionary
	"""
	def draw_figure(self, event=None):
		if event:
			name = event.widget.cget('text')
			for (x, y) in self.patterns[name]:
				self.set_pattern_cell(x, y)

	""" 
	Method set_pattern_cell
	Similar to change_cell_state, but with reduced functionality
	changes the state of a cell
	"""
	def set_pattern_cell(self, x, y):
		try:
			ratio = self.width // self.cell_size
			cell = self.cells[x + ratio * y]
			# Update Field cell
			self.field.set_cell(x, y)
			# Update local cell
			self.canvas.itemconfig(cell, fill='gray')
		except IndexError as e:
			pass

	""" 
	Method change_cell_state
	Alters the state of a cell (in some cases exception with reading the coordinates appears)
	Finds the index (x, y) of the cell form the canvas
	Updates local rectangle and updates Field object
	"""
	def change_cell_state(self, event):
		# Calculation of the indexes
		x, y = event.x, event.y
		id_x = x // self.cell_size
		id_y = y // self.cell_size
		ratio = self.width // self.cell_size

		# Handling IndexError (wrong coordinates interpretation near the bottom borders)
		try:
			cell = self.cells[id_x + ratio * id_y]

			# Update Field cell
			self.field.set_cell(id_x, id_y)

			# Update local cell
			if event.widget.itemcget(cell, 'fill') == 'gray':
				event.widget.itemconfig(cell, fill='white')
			else:
				event.widget.itemconfig(cell, fill='gray')
		except IndexError as e:
			pass

	"""
	clear_field method
	Cleans entire screen and also wipes the Field object
	"""
	def clear_field(self):
		if self.thread:
			self.thread.condition = False
		for cell in self.cells:
			self.canvas.itemconfig(cell, fill='white')
		self.field.clean()

	"""
	start method
	Saves field object and inits main loop of the GUI
	"""
	def start(self, field):
		self.field = field
		self.root.mainloop()

	"""
	stop method
	Event-handler for the Stop button
	Stops the Drawer thread (autoupdater)
	"""
	def stop(self):
		if self.thread:
			self.thread.condition = False

	"""
	start_game method
	Event-handler for the Start button
	1) Makes one step
	2) Starts the Drawer thread (autoupdater) if this option is activated 
	"""
	def start_game(self):
		self.update_canvas()
		if self.thread_active:
			self.start_thread(0.2)

	"""
	start_thread method
	Starts the Drawer thread (autoupdater)
	Initializes background thread for updating the canvas after short pause
	"""
	def start_thread(self, delay):
		sleep(0.1)
		self.thread = Drawer(self, delay)
		self.thread.setDaemon(True)
		self.thread.start()
		

	"""
	canvas_to_field method
	Transforms the canvas to two-dimensional array of booleans for Field object
	"""
	def canvas_to_field(self):
		# Init new 2D-array
		field = [[False for x in range(self.cells_params[0])] for y in range(self.cells_params[1])]
		for i in range(len(self.cells)):
			if self.canvas.itemcget(self.cells[i], 'fill') == 'gray':
				field[i // self.cells_params[0]][i % self.cells_params[0]] = True

		return field

	"""
	update_canvas method
	1) Requests 2D array copy of canvas
	2) Processes it and receives new field and condition
	3) Transforms new field to a new canvas
	4) Returns the condition of the map (may be it ended)
	"""
	def update_canvas(self):
		field = self.canvas_to_field()
		new_field, condition = self.field.process_field(field)
		self.update_cells(new_field)

		return condition

	"""
	update_cells method
	Step by step updates the cells and redraws them
	"""
	def update_cells(self, field):
		for i in range(len(field)):
			for j in range(len(field[0])):
				index = i + self.cells_params[0] * j
				if field[i][j]:	
					self.canvas.itemconfig(self.cells[index], fill='gray')
				else:
					self.canvas.itemconfig(self.cells[index], fill='white')