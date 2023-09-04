#!/usr/bin/python3
"""module: 2-rectangle
This is a Rectangle class."""


class Rectangle:
    """Create a Rectangle object."""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle object's width and height."""

        self.__width = width
        self.__height = height

    @property
    def width(self):
        """method: set_width getter"""

        if (not isinstance(self.__width, int)) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, width):
        """method: set_width"""

        if not isinstance(self.__width, int) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

    @property
    def height(self):
        """method: set_height getter"""

        if (not isinstance(self.__height, int)) or isinstance(self.__height, bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        return self.__height

    @height.setter
    def height(self, height):
        """method: set_height"""

        if not isinstance(self.__height, int) or isinstance(self.__height, bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    """calculate area of Rectangle object."""

    def area(self):
        return self.__height * self.__width

    """calculate perimeter of Rectangle object."""

    def perimeter(self):
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height + self.width) * 2
