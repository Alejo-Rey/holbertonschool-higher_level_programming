#!/usr/bin/python3
''' class model Base '''
import json
import turtle


class Base:
    ''' create a init file '''

    f = open("__init__.py", "w+")
    __nb_objects = 0

    def __init__(self, id=None):
        ''' constructor to instance '''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' method to return a string type json '''
        if list_dictionaries is not None or len(list_dictionaries) < 1:
            return (json.dumps(list_dictionaries))
        else:
            return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        ''' method to create a file with the name of the class  '''
        l = []
        if list_objs is not None:
            for x in list_objs:
                l.append(x.to_dictionary())
        with open("{}.json".format(cls.__name__), 'w') as f:
            f.write(cls.to_json_string(l))

    @staticmethod
    def from_json_string(json_string):
        ''' method that return a list of JSON string '''
        if json_string is None:
            return ([])
        return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        ''' method to return an instance '''
        return super()

    @staticmethod
    def draw(list_rectangles, list_squares):
        ''' method turtle change '''
        for i in list_rectangles:
            turtle.penup()
            turtle.home()
            turtle.color("blue")
            turtle.setpos(i.x, i.y)
            turtle.pendown()
            turtle.forward(i.height)
            turtle.left(90)
            turtle.forward(i.width)
            turtle.left(90)
            turtle.forward(i.height)
            turtle.left(90)
            turtle.forward(i.width)

        for i in list_squares:
            turtle.penup()
            turtle.home()
            turtle.color("red")
            turtle.setpos(i.x, i.y)
            turtle.pendown()
            turtle.forward(i.size)
            turtle.left(90)
            turtle.forward(i.size)
            turtle.left(90)
            turtle.forward(i.size)
            turtle.left(90)
            turtle.forward(i.size)
        turtle.exitonclick()
