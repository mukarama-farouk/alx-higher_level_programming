#!/usr/bin/python3
"""A class Rectangle that defines a rectangle by height and width
"""


class Rectangle:
    """class Rectangle"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Instantiating width and height"""
        self.width = width
        self.height = height
        """Incremented during each new instance instantiation"""
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of a rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Returns the perimeter of a rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Prints the rectangle with the character #
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return ("\n".join(["".join(["#" for i in range(self.__width)])
                for j in range(self.__height)]))

    def __repr__(self):
        """return a string representation of the rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of Rectangle"""
        print("Bye rectangle...")
        """Decremented during each new instance deletion"""
        Rectangle.number_of_instances -= 1
