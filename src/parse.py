"""
gitao - parse.py

Argument parse control
"""

import sys
from typing import List, Tuple

from flags import Flags # flags.py


def parseArguments() -> Tuple[str, List[str], Flags]:
	""" Process sys.argv to get command, arguments and flags """

	# Ignore `sys.argv[0]` and empty args
	argv: List[str] = [arg for arg in sys.argv[1:] if len(arg)]

	# From argv, separate flags and arguments
	args:  List[str] = [v for v in argv if v[0] != '-']
	flags: List[str] = [v for v in argv if v[0] == '-']

	# Fixing args that start with an escaped hyphen
	for i in range(len(args)):
		if args[i].startswith(r'\-'):
			args[i] = args[i][1:]  # Ignore r'\' at [0]

	# Safe equivalent to: `command = args.pop(0)`
	command: str = args[0] if len(args) else ''
	args = args[1:]

	flags_object = Flags(flags) # `flags` parsing can cause termination

	return (command, args, flags_object)
