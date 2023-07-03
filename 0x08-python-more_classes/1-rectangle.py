#!/usr/bin/python3
"""A class Rectangle that defines a rectangle by height and width
"""

class Rectangle:
    """class Rectangle"""
    def __init__(self, width=0, height=0):
        """Instantiating width and height
        """
        self.width = width
        self.height = height
    @property
    def width(self):
        """Property width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """width setter
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """height setter
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
