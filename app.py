#/usr/bin/python3
import field
import interface

'''
Width and height of the window
Size of the rectangle (cell) should be a divisor of width & height
Initializes Tkinter GUI
'''
def main():
	width = 800
	height = 600
	size = 20 # 10
	# Tkinter GUI
	window = interface.Window(width=width, height=height, cell_size=size, thread_active=True)
	# Field class for logic
	f = field.Field(*window.cells_params)
	# Run the main loop
	window.start(f)

if __name__ == '__main__':
	main()