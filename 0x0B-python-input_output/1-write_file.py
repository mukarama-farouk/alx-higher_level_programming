#!/usr/bin/python3
"""A module that writes a string to a file"""


def write_file(filename="", text=""):
    """This function writes a string to a text file

    Args:
        filename: filename
        text: text to be written

    Returns:
        The number of characters written

    Raises:
        None

    """

    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
