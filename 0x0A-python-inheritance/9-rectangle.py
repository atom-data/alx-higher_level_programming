#!/usr/bin/python3
"""Definition of class Base Geometry and Rectangle"""


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


class Rectangle(BaseGeometry):
    """Subclass of BaseGeometry"""

    def __init__(self, width, height):
        """Initialize a rectangle
        Args:
        width (int): width of the rectangle
        height (int): height of the rectangle
        """
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Compute area of rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        """Informal string representation of rectangle"""
        return f"[Rectangle] {self.__width}/{self.__height}"
