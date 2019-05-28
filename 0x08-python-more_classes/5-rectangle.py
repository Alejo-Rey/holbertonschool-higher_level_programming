#!/usr/bin/python3
"""
function to define a rectangle
"""


class Rectangle:
    """ atributes and methods """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__heigh

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value

    def area(self):
        return (self.__height * self.__width)

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__height + self.__width))

    def __str__(self):
        array = []
        if self.__width == 0 or self.__height == 0:
            return (''.join(array))
        for x in range(self.__height):
            for y in range(self.__width):
                array.append("#")
            if x < self.__height - 1:
                array.append('\n')
        return (''.join(array))

    def __repr__(self):
        r = "Rectangle("
        return (r + repr(self.__width) + ", " + repr(self.__height) + ")")

    def __del__(self):
        print("Bye rectangle...")
