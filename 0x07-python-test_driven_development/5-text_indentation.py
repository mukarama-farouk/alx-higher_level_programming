#!/usr/bin/python3
"""A module that contains a function that prints a text"""


def text_indentation(text):
    """This function prints a text with 2 new lines after
    each of these characters: ., ? and :

    Args:
        text: Must be a string

    Returns:
        No return

    Raises:
        TypeError: If text isnt a string

    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ".?:"

    text_copy = text[:]

    for i in chars:
        text_list = text_copy.split(i)

        text_copy = ""

        for j in text_list:
            j = j.strip(" ")
            text_copy = j + i if text_copy == "" else text_copy + "\n\n"
            + j + i

    print(text_copy[:-3], end="")
