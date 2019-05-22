#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    z = 0
    for y in my_list:
        if z != x:
            try:
                z = z + 1
                print("{:d}".format(y), end="")
            except (TypeError, ValueError):
                z -= 1
                pass
    print()
    return (z)
