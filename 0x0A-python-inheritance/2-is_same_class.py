#!/usr/bin/python3
"""Define is_same_class function"""


def is_same_class(obj, a_class):
    """Determine an exact class instance

    Args:
    obj : an object
    a_class: a class

    Returns:
    (bool) : Truth value of object belonging
    """
    return(type(obj) == a_class)
