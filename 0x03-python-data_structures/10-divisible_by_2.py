#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return (None)
    my_list2 = my_list.copy()
    for x in range(len(my_list) - 1):
        if my_list[x] % 2 == 0:
            my_list2[x] = True
        else:
            my_list2[x] = False
    return (my_list2)
