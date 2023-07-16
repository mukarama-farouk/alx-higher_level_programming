#!/usr/bin/python3
"""This module contains a class Rectangle that inherits from class Base"""

from models.base import Base


class Rectangle(Base):
    """Represents a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """instantiates the class Rectangle

        Args:
            width: wifth of the rectangle
            height: Height of rectangle
            x: X coordinate of rectangle
            y: y coordinate of rectangle
            id: identity of the new class rectangle

        Raises:
            TypeError: If either of width or height is not an integer.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an integer.
            ValueError: If either of x or y < 0.

        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Sets/gets the width of the Rectangle."""
        return self.__width


    @property
    def height(self):
        """sets/gets the width of the Rectangle."""
        return self.__height


    @property
    def x(self):
        """Sets/gets the x coordinate of the Rectangle"""
        return self.__x


    @property
    def y(self):
        """Sets/gets the y coordinate of the Rectangle"""
        return self.__y


    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value


    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value


    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value


    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value



    def area(self):
        """returns the area value of the Rectangle instance"""
        return self.width * self.height
