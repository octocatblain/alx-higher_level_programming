#!/usr/bin/python3
"""module: rectangle eval is magic"""


class Rectangle:
    """class: Rectangle"""

    def __init__(self, width=0, height=0):
        """Initialize Rectangle object's width and height."""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """method: set_width"""
        if (not isinstance(self.__width, int)) or isinstance(self.__width, bool):
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        return self.__width

    @width.setter
    def width(self, width):
        """method: set_width setter"""
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
        """method: set_height setter"""
        if not isinstance(self.__height, int) or isinstance(self.__height, bool):
            raise TypeError("height must be an integer")
        if self.__height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    def area(self):
        """method: area"""
        return self.__height * self.__width

    def perimeter(self):
        """method: perimeter"""
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__height + self.width) * 2

    def __str__(self):
        """method: __str__"""
        ret_str = ""
        if self.__height == 0 or self.__width == 0:
            return ""
        for idx in range(self.__height):
            ret_str += "#" * self.width
            if idx + 1 < self.__height:
                ret_str += "\n"
        return ret_str

    def __repr__(self):
        """method: __repr__"""
        ret_str = "Rectangle(" + str(self.__width) + ","
        ret_str += str(self.__height) + ")"
        return ret_str
