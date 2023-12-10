#!/usr/bin/python3
"""
Class Square: Represents a square object initialized with size.
"""

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
            size (int): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Calculate and return the area of the Square.

        Returns:
            int: The area of the square.

        """
        return self.__size * self.__size
