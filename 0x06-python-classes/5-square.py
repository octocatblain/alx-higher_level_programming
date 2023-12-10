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
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The size of the square.

        """
        return self.__size

    @size.setter
    def size(self, size):
        """
        Set the size of the square.

        Args:
            size (int): The size of the square.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.size * self.size

    def my_print(self):
        """
        Print the square using '#' characters.

        """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            for _ in range(self.__size):
                print("#", end="")
            print()
