#!/usr/bin/python3
"""A class defining a square (based on 1-square.py)"""

class Square:
    """
    Class Square with private instance attribute size.

    Attributes:
        __size (int): The size of the square.

    """

    def __init__(self, size=0):
        """
        Initialize the square with a given size.

        Args:
            size (int): The size of the square.

        """
        self.__size = size
