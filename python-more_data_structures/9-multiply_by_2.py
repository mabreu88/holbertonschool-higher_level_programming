#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    cp_dict = a_dictionary.copy()
    for x, y in cp_dict.items():
        cp_dict[x] = y * 2
    return cp_dict
