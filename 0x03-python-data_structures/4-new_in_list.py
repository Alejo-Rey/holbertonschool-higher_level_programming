#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    x = len(my_list) - 1
    if idx > x or idx < 0:
        return (my_list.copy())
    copy_list = my_list.copy()
    copy_list[idx] = element
    return (copy_list)
