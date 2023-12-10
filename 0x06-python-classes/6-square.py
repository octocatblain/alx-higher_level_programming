#!/usr/bin/python3
"""
Class Square: Represents a square object initialized with size and position.
"""

class Square:
    """
    Class Square with private instance attributes size and position.

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The position of the square.

    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the square with a given size and position.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.

        """
        self.size = size
        self.position = position

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

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The position of the square.

        """
        return self.__position

    @position.setter
    def position(self, position):
        """
        Set the position of the square.

        Args:
            position (tuple): The position of the square.

        Raises:
            TypeError: If position is not a tuple of two positive integers.

        """
        if type(position) != tuple or len(position) != 2 or \
                type(position[0]) != int or type(position[1]) != int or \
                position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of two positive integers")
        self.__position = position

    def area(self):
        """
        Calculate and return the area of the square.

        Returns:
            int: The area of the square.

        """
        return self.size * self.size

    def my_print(self):
        """
        Print the square using '#' characters and position.

        """
        if self.__size == 0:
            print()
            return

        for _ in range(self.__position[1]):
            print()
        
        for _ in range(self.__size):
            for _ in range(self.__position[0]):
                print(" ", end="")
            for _ in range(self.__size):
                print("#", end="")
            print()
