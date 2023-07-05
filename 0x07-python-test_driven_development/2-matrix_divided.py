#!/usr/bin/python3
"""A odule which contains a function that divivdes a matrix"""


def matrix_divided(matrix, div):
    """A matrix function

    args:
        matrix: a list of list(floats/integers)
        div: a number(float/integer)

    Return:
        a new matrix of the division

    Raises:
        TypeError: If the matrix isnt a list of list of numbers
                   If the rows of the matrix isnt of thesame size
                   If the div isnt an integer/float

        ZeroDivisionError: If div is 0

    """
    matrix_msg = "matrix must be a matrix (list of lists) of integers/floats"

    if not matrix or not isinstance(matrix, list):
        raise TypeError(matrix_msg)

    row_len = 0
    row_msg = "Each row of the matrix must have the same size"

    for items in matrix:
        if not items or not isinstance(items, list):
            raise TypeError(matrix_msg)

        if row_len != 0 and len(items) != row_len:
            raise TypeError(row_msg)

        for number in items:
            if not isinstance(number, (int, float)):
                raise TypeError(matrix_msg)

        row_len = len(items)

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(y / div, 2) for y in x] for x in matrix]
    return new_matrix
