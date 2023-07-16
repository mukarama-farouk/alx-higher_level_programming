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
