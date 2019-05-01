#!/usr/bin/python3
def print_last_digit(number):
    int_last = int(str(number)[-1:])
    print("{:d}".format(int_last), end="")
    return (int_last)
