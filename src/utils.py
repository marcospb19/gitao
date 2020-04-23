#
# gitao - utils.py
#

import sys


def printerr(*args, **kwargs):
    print(*args, file = sys.stderr, **kwargs)
