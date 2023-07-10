#!/usr/bin/python3
"""
modulethat chescks if an object is an instance of a class"""


def inherits_from(obj, a_class):
    """returns True if the object is an instance of a class
       that inherited (directly or indirectly) from the specified class;
       or False if otherwise.
    """
    if type(obj) != a_class:
        return issubclass(type(obj), a_class)
    else:
        return False
