#!/usr/bin/python3
"""Define an attribute addition function"""


def add_attribute(obj, attribute, value):
    """Add attribute to an object

    Args:
    obj (instance): instance of a class
    attribute(string): name of attribute to be added
    value: value of attribute to be added
    """

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add a new attribute")
    setattr(obj, attribute, value)
