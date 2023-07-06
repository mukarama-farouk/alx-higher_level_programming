#!/usr/bin/python3
"""This module contains a function that prints a square with the character #"""


def print_square(size):
    """This is a print square function

    args:
        size: size length of the square

    Return:
        No return

    Raises:
        TypeError: If size isnt an integer number
                   If size is a float number and < 0

        ValueError: If size < 0

    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for i in range(size):
        print("#" * size)
