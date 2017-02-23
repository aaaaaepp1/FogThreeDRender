import sys
import os

def main():
	filename = os.path.join(os.getcwd(), 'a.txt')

	if os.path.exists(filename) and os.path.isfile(filename):
		pass
	else:
		print 'error to find the motion data file path'
		sys.exit(1)

	a_command_list = []
	with open(filename, "rU") as a_file:
		while True:
			a_string = a_file.readline()
			if len(a_string) == 0: break
			output = ''
			for char in a_string:
				if char != '\n': output = output + char
			print "{}, {}, {}".format(output, len(output), [char for char in output])


if __name__ == '__main__':
	sys.exit(main())