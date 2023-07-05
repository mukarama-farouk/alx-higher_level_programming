#!/usr/bin/python3
"""This module contains a function that prints My name is
<first name> <last name>"""


def say_my_name(first_name, last_name=""):
    """A function that print strings

    args:
        first_name: Must be string
        last_name: Must be string

    Raises:
        TypeError: If first_name and last_name arent strings

    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
