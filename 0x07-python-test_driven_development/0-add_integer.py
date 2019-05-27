#!/usr/bin/python3
"""
function to add two numbers

"""


def add_integer(a, b=98):
    """
    conditionals before return
    """
    if not isinstance(a, int):
        if not isinstance(a, float):
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if not isinstance(b, float):
            raise TypeError("b must be an integer")
    c = int(a) + int(b)
    return (c)
