#!/usr/bin/python3
"""A module that multiplies two matrices
"""

def matrix_mul(m_a, m_b):
    """This function multiplies two matrices

    args:
        m_a - must be a list of list of integers/float
        m_b - must be a list of list of integers/float

    Returns:
        The product of the multiplication(a new matrix)

    Raises:
        TypeError: If the args arent list
                   If the args arents a list of list
                   If the args are empty
                   if one element of those list of lists is not an integer or a float
                   If either of the args is not a rectangle
        ValueError: If either of the args is empty
                    If the args cant be multiplied
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    for elements in m_a:
        if not isinstance(m_a, list):
            raise TypeError("m_a must be a list of lists")

    for elements in m_b:
        if not isinstance(m_b, list):
            raise TypeError("m_b must be a list of lists")

    if len(m_a) == 0 or (len(m_a) == 1 and len(m_a[0]) == 0):
        raise ValueError("m_a can't be empty")

    if len(m_b) == 0 or (len(m_b) == 1 and len(m_b[0]) == 0):
        raise ValueError("m_b can't be empty")

    for lists in m_a:
        for elements in lists:
            if not isinstance(elements, (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for lists in m_b:
        for elements in lists:
            if not isinstance(elements, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    
    length = 0

    for elements in m_a:
        if length != 0 and length != len(elements):
            raise TypeError("each row of m_a must be of the same size")
        length = len(elements)

    length = 0

    for elements in m_b:
        if length != 0 and length != len(elements):
            raise TypeError("each row of m_b must be of the same size")
        length = len(elements)

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    result = [[sum(a[i] * m_b[i][j] for i in range(len(m_a[0]))) for j in range(len(m_b[0]))] for a in m_a]

    return result

    







    
