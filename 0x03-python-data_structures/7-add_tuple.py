#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    a, b = len(tuple_a), len(tuple_b)

    if a == 2 == b or a > 2 or b > 2:
        return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    if b == 1:
        return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + 0))
    if b == 0:
        return ((tuple_a[0] + 0), (tuple_a[1] + 0))
