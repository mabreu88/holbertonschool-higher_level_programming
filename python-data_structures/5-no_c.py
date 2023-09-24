#!/usr/bin/python3
def no_c(my_string):
    new_str = ''
    for x in my_string:
        if x != 'C' and x != 'c':
            new_str += x
    return new_str
