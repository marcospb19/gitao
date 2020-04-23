"""
gitao - gitao.py

Main file
"""

import parse # parse.py


def main() -> None:
	""" Main function """

	command, arguments, flags = parse.parseArguments()


if __name__ == '__main__':
	main()
