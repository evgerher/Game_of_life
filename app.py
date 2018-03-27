#/usr/bin/python3
import field
import interface
import json

"""
Read json file and through file not found exceptions
"""
def read_json(file_name):
	with open(file_name, encoding='utf-8') as json_file:
		return json.load(json_file)

'''
Width and height of the window
Size of the rectangle (cell) should be a divisor of width & height
Initializes Tkinter GUI
'''
def main():
	try:
		config = read_json('config.json')
		patterns = read_json('patterns.json')

		width = config['width']
		height = config['height']
		size = config['size'] # 10
		# Tkinter GUI
		window = interface.Window(width=width, height=height, cell_size=size, thread_active=False, patterns=patterns)
		# Field class for logic
		f = field.Field(*window.cells_params)
		# Run the main loop
		window.start(f)
	except FileNotFoundError as e:
		print("No such file")

if __name__ == '__main__':
	main()