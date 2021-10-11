#!/usr/bin/python3
"""
class checker
"""


def is_same_class(obj, a_class):
    """
    function to check if an object is an instance of a class
    Args:
            obj (object): the object
            a_class (class): the class
    Returns:
            True: if object is an instance of the class
            False: if object is not an instance of the class
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
