#!/usr/bin/python3
"""A square module that inherits from rectangle class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents a square"""


    def __init__(self, size, x=0, y=0, id=None):
        """Instantiates the new class Square

        Args:
            size: sixe of square
            x: x coordinate of new class square
            y: y coordinate of new class square
            id: identification of new class square

        """

        super().__init__(size, size, x, y, id)


    @property
    def size(self):
        """sets/gets size of square"""
        return self.width


    @size.setter
    def size(self, value):
        self.width = value
        self.height = value




            
