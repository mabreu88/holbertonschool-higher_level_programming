#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_n = min(my_list)
    for x in my_list:
        if x > max_n:
            max_n = x
    return max_n
