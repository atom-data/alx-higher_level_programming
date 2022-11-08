#!/usr/bin/python3
"""
Define the function lookup()
"""


def lookup(obj):
    """Determine liost of available attributes
    Returns:
    List of attributes of objects
    """
    return(dir(obj))
