#!/usr/bin/python3
''' class Square '''
from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        ''' constructor of Square '''
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' getter of size '''
        return super().width

    @size.setter
    def size(self, value):
        ''' setter of size '''
        super(Square, self.__class__).width.fset(self, value)
        super(Square, self.__class__).height.fset(self, value)

    def __str__(self):
        ''' method string '''
        return (
                "[Square] (" +
                str(self.id) +
                ") " +
                str(self.x) +
                "/" +
                str(self.y) +
                " - " +
                str(self.size)
                )

    def update(self, *args, **kwargs):
        ''' method to update with args and kwargs '''
        if args:
            l = ['id', 'size', 'x', 'y']
            for arg in range(len(args)):
                setattr(self, l[arg], args[arg])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        ''' methof to return an dictionary '''
        new_dict = dict()
        new_dict['id'] = self.id
        new_dict['size'] = self.size
        new_dict['x'] = self.x
        new_dict['y'] = self.y
        return new_dict
