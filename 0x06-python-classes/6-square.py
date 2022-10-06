#!/usr/bin/python3
"""Define the class Square"""


class Square:
    """Representation of a square

    Attributes:
    __size (int): The length of a side of a square
    __position (tuple): position of the square in 2-dimensional space
    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the class square

        Args:
        size (int): The length of a side of a square
        position (tuple): position of the square in 2-dimensional space
        """
        self.size = size
        self.position = position

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

    def my_print(self):
        """Print a square"""
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print("")
        for j in range(self.__size):
            print("".join([" " for k in range(self.__position[0])]), end="")
            print("".join(['#' for j in range(self.__size)]))

    @property
    def position(self):
        """getter for __position

        Returns:
        The position of a square in a plane
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Assign value to __position

        Args:
        value (tuple): position of the square on the plane
        """
        if type(value) is not tuple or len(value) != 2 or \
            type(value[0]) is not int or value[0] < 0 or \
                type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        else:
            self.__position = value
