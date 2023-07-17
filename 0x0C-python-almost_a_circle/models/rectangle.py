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


    def display(self):
        """Print the Rectangle using the `#` character."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)


    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"



    def update(self, *args, **kwargs):
        """Updating the rectangle class

        Args:
            *args: (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute

            *kwargs: (dict): New key/value pairs of attributes.
        """

        if args and len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.width = arg
                elif a == 2:
                    self.height = arg
                elif a == 3:
                    self.x = arg
                elif a == 4:
                    self.y = arg
                a += 1

        elif kwargs and len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def to_dictionary(self):
        """Return the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
