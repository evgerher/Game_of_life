import tkinter as tk

cells = []
width = 800
height = 400
cell_size = 20

def change_cell_state(event):
	x, y = event.x, event.y
	global cells
	id_x = x // cell_size
	id_y = y // cell_size
	ratio = width // cell_size
	cell = cells[id_x + ratio * id_y]
	event.widget.itemconfig(cell, fill='gray')

def start_game(event):
	pass

def clear_field(event):
	pass

root = tk.Tk()

geometry = '{}x{}'.format(width, height)
root.geometry(geometry)

canvas = tk.Canvas(root, width=width, height=height)
for i in range(height // cell_size):
	for j in range(width // cell_size):
		cells.append(canvas.create_rectangle(j * cell_size, i * cell_size, (j+1) * cell_size, (i+1) * cell_size, fill='white'))

canvas.pack(fill=tk.BOTH)

canvas.bind('<Button 1>', change_cell_state)
canvas.bind('<B1-Motion>', change_cell_state)

frame = tk.Frame(root)

btn_start = tk.Button(frame, text='Start', command=start_game)
btn_clear = tk.Button(frame, text='Clear', command=clear_field)

frame.pack(side='bottom')
btn_start.pack(side='left')
btn_clear.pack(side='right')


root.mainloop()