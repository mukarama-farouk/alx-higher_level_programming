#!/usr/bin/python3
"""This model defines a class Base"""
import json
import csv
import turtle


class Base:
    """Represents the “base” of all other classes in this project

    Attributes:
        __nb_objects (int): The number of instantiated Bases
    """

    __nb_objects = 0


    def __init__(self, id=None):
        """class constructor

        Args:
            id: An integer which is the identity of the new base

        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
