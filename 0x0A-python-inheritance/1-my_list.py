#!/usr/bin/python3
''' funtion to print a list inherit '''


class MyList(list):
    ''' Class Mylist to print sorted '''
    def __init__(self):
        list.__init__(self)

    def print_sorted(self):
        ''' function to return a sorted list '''
        print(sorted(self))
