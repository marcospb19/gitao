"""
gitao - utils.py

Common utility functions used by gitao
"""

import sys


def printerr(*args, **kwargs):
    print(*args, file = sys.stderr, **kwargs)
