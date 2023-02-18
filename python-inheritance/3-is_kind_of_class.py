#!/usr/bin/python3
"""Third"""


def is_kind_of_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified class
    otherwise False
    Args:
        obj (obj): object
        a_class (class): a class to compare to
    """
    if isinstance(obj, a_class):
        return True
    return False
