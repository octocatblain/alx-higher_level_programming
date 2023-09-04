#!/usr/bin/python3
"""Print square module."""


def print_square(size):
    """Print square function."""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        for _ in range(size):
            print("#", end="")
        print()
