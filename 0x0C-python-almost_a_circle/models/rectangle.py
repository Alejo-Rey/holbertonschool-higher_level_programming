#!/usr/bin/python3
''' class Rectangle inherit of base '''
from models.base import Base


class Rectangle(Base):
    '''class to define a rectangle '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' constructor of Rectangle '''
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        ''' getter width '''
        return self.__width

    @width.setter
    def width(self, value):
        ''' setter of width '''
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        ''' getter of height '''
        return self.__height

    @height.setter
    def height(self, value):
        ''' setter of height '''
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        ''' getter of x '''
        return self.__x

    @x.setter
    def x(self, value):
        ''' setter of x '''
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        ''' getter of y '''
        return self.__y

    @y.setter
    def y(self, value):
        ''' setter of y '''
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        ''' method to return an area of the class '''
        return (self.width * self.height)

    def display(self):
        ''' method to display # of th class '''
        for y in range(self.y):
            print()
        for h in range(self.height):
            for x in range(self.x):
                print(end=" ")
            for w in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        ''' methdo strign to print '''
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
        ''' method to update with args and kwargs '''
        if args:
            l = ['id', 'width', 'height', 'x', 'y']
            for arg in range(len(args)):
                setattr(self, l[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        ''' method to return a dictionary '''
        new_dict = dict()
        new_dict['id'] = self.id
        new_dict['width'] = self.width
        new_dict['height'] = self.height
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        return new_dict
