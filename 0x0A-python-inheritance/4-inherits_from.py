#!/usr/bin/python3
"""Determine subclass membership"""


def inherits_from(obj, a_class):
    """Determine subclass membership

    Args:
    obj: An whose subclass membership is to be determined
    a_class: subclass

    Returns:
    bool: True if object belongs to subclass else false
    """
    return(issubclass(type(obj), a_class) and
           not issubclass(a_class, type(obj)))
