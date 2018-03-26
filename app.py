#/usr/bin/python3
import field
import interface

def main():
	window = interface.Window()
	f = field.Field(*window.cells_params)
	window.start(f)


if __name__ == '__main__':
	main()