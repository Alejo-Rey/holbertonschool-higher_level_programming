#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        z = 0
        for y in my_list:
            if z != x:
                z = z + 1
                print("{}".format(y), end="")
        print()
        return (z)

    except:
        z = 0
        print(my_list)
        for y in my_list:
            z = z + 1
        return (z)
