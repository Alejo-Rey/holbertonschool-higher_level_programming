#!/usr/bin/python3
def element_at(my_list, idx):
    x = len(my_list) -1
    if idx < 0 or idx > x:
        return(None)
    return(my_list[idx])
