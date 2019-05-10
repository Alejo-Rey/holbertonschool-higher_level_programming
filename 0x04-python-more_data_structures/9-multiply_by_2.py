#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    n = {}
    for x in a_dictionary:
        y = a_dictionary[x] * 2
        n[x] = y
    return (n)
