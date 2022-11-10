#!/usr/bin/python3
"""Definition of class Base Geometry"""


class BaseGeometry:
    """Base Geometry"""

    def area(self):
        """Force an error"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value
        Args:
        name (string): Element of error message
        value (int): number to be validated
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than zero")
