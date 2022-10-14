#!/usr/bin/python3
"""
Defines a class Rectangle
"""


class Rectangle:
    """Representation of a rectangle"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.height = height
        self.width = width
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Compute the area of a rectangle

        Returns:
        The area of a rectangle
        """
        return (self.width * self.height)

    def perimeter(self):
        """Compute the perimeter of the rectangle

        Returns:
        The perimeter of a rectangle
        """
        if (self.width == 0 or self.height == 0):
            return 0
        return (2 * (self.width + self.height))

    def __str__(self):
        """Printable string representation of a rectangle"""
        string = ""
        if (self.__width != 0 and self.__height != 0):
            string += "\n".join(
                    str(Rectangle.print_symbol) * self.__width
                    for j in range(self.__height))
        return string

    def __repr__(self):
        """Informal string representation of a rectangle"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """An instance destructor method for rectangles"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compare areas of rectangles"""
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif (not isinstance(rect_2, Rectangle)):
            raise TypeError('rect_2 must be an instance of Rectangle')
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """Square instances of Rectangle"""
        return cls(size, size)
