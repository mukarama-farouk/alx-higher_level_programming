#!/usr/bin/python3

def add_integer(a, b=98):
    """This functions adds two integers/float

    Args:
        a: First integer/float number
        b: Second integer/fload number

    Returns:
        The addidtion of the two integer/float numbers

    Raises:
       TypeError: if a or b arent interger/float numbers

    """

    if type(a) not in [int,float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
