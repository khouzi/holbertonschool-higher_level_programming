#!/usr/bin/python3
"""
function write file
"""


def write_file(filename="", text=""):
	"""
    write file function
    Args:
        filename(string): the given file name
        text(string): the text
    Returns:
        number of characters written.
    """
	with open(filename, mode ="w", encoding="utf-8") as myfile:
		return myfile.write(text)