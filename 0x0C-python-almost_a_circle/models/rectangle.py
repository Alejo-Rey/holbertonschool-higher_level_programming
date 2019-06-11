#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError ("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
       return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return (self.width * self.height)

    def display(self):
        for y in range(self.y):
            print()
        for h in range(self.height):
            for x in range(self.x):
                print(end=" ")
            for w in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        string = (
                "[Rectangle] (" +
                str(self.id) +
                ") " +
                str(self.x) +
                "/" +
                str(self.y) +
                " - " +
                str(self.width) +
                "/" +
                str(self.height)
                )
        return (string)
    def update(self, *args, **kwargs):
        if args is not None:
            l = len(args)
            if l == 1:
                self.id = args[0]
            elif l == 2:
                self.width = args[1]
            elif l == 3:
                self.height = args[2]
            elif l == 4:
                self.x = args[3]
            elif l == 5:
                self.y = args[4]
            data = {}
            for key, value in kwargs.items():
                data[key] = value
                if key == 'id':
                    self.id = data[key]
                if key == 'height':
                    self.height = data[key]
                if key == 'width':
                    self.width = data[key]
                if key == 'x':
                    self.x = data[key]
                if key == 'y':
                    self.y = data[key]

