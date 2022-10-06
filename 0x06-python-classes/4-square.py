#!/usr/bin/python3
"""Define the class Square"""


class Square:
    """Representation of a square

    Attributes:
    __size (int): The length of a side of a square
    """
    def __init__(self, size=0):
        """Initializes the class square

        Args:
        size (int): The length of a side of a square
        """
        self.size = size

    def area(self):
        """Compute the area of a square

        Returns:
        The area of a square
        """
        return (self.__size) ** 2

    @property
    def size(self):
        """getter of __size attribute

        Returns:
        The value of __size attribute
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Assign value to __size

        Args:
        value (int): The length of a side of a square
        """
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        else:
            self.__size = value
