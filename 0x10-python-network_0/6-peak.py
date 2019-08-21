#!/usr/bin/python3
''' function find a peak '''


def find_peak(list_of_integers):
    ''' fuction to know the ig number of the list'''
    n = len(list_of_integers)

    if n == 0:
        return(None)

    r = 0
    for x in range(n):
        if list_of_integers[x] > r:
            r = list_of_integers[x]
    return(r)
