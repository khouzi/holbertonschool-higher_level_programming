#!/usr/bin/python3
"""
function read file
"""


def read_file(filename=""):
    """
Read file function
Args:
    filename(string): the given file name
"""
    with open(filename, encoding="utf-8") as myfile:
        print(myfile.read())
