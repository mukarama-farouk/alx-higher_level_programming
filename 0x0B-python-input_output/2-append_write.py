#!/usr/bin/python3
"""A module that appends in a file"""

def append_write(filename="", text=""):
    """This functions appends a string at the end of a text file

    Args:
        filename: Name of file to be appended
        text: Text to be appended

    Return:
        The the number of characters added

    Raises:
        None

    """

    with open(filename, 'a', encoding="UTF8") as f:
        return f.write(text)
