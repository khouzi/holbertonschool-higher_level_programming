#!/usr/bin/python3
"""
function append file
"""


def append_write(filename="", text=""):
    """ append function
    Args:
        filename(string): the given file name
        text(string): the text
    Returns:
        number of characters added.
    """
    with open(filename, mode="a", encoding="utf-8") as myfile:
        return myfile.write(text)
