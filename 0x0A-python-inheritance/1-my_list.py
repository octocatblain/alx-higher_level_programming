#!/usr/bin/python3
"""My list function that inherits from list"""


class MyList(list):
    """my list function"""

    def print_sorted(self):
        """Print function."""
        print(sorted(self))
