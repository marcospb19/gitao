#
# gitao - parse.py
#

import sys
from typing import List

from flags import Flags  # flags.py


def parseArguments():

	# Ignore first argument and ignore first one
	argv: List[str] = [arg for arg in sys.argv[1:] if len(arg)]

	# From argv, separate flags and arguments
	flags:     List[str] = [v for v in argv if v[0] == '-']
	arguments: List[str] = [v for v in argv if v[0] != '-']

	# Fixing arguments that start with an escaped hyphen
	for i in range(len(arguments)):
		if arguments[i].startswith(r'\-'):
			arguments[i] = arguments[i][1:]  # Ignore r'\' at [0]

	# Parse flags filling the class Flags
	flags: Flags = Flags(flags)

	# Safely selecting main command from arguments[0]
	command: str = ''
	if len(arguments):
		command   = arguments[0]
		arguments = arguments[1:]

	return (command, arguments, flags)
