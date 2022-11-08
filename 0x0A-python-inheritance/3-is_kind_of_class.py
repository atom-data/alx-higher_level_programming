#!/usr/bin/python3
"""Define is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """Determine class membership or  inheritance

    Args:
    obj: An object whose membership is to be determined
    a_class: A class whose object is to be determined

    Returns:
    (bool): Returns True membership or inheritance is determined else False
    """
    return(isinstance(obj, a_class))
