#!/usr/bin/python3
"""A module for reading a file"""

def read_file(filename=""):
    """This function reads a text file and prints it on stdout

    Args:
        filename - filename

    Raises:
        None

    """

    with open(filename, 'r', encoding="utf-8") as file:
        read_file = file.read()
        print(read_file, end='')
