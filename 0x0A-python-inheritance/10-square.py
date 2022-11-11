#!/usr/bin/python3
"""Definition of class Square"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Definition of a square"""

    def __init__(self, size):
        """Initialize a square

        Args:
        size (int): length of side of a square
        """
        super().__init__(size, size)
        self.__size = size

        def area(self):
            """Compute area of a square"""
            return super().area()
