#!/usr/bin/python3
class Square:
    """Initialize Class Square."""

    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.size * self.size

    def my_print(self):
        if self.__size == 0:
            print()
            return

        for _ in range(self.__size):
            for _ in range(self.position[0]):
                print("_", end="")
            for _ in range(self.__size):
                print("#", end="")
            print()
