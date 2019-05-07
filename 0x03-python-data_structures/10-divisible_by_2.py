#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is not None:
        my_list2 = []
        for x in range(len(my_list)):
            if my_list[x] % 2 == 0:
                my_list2.append(True)
            else:
                my_list2.append(False)
        return (my_list2)
