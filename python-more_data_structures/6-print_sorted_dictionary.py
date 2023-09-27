#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dict = sorted(a_dictionary.items())
    for x, y in dict:
        print('{0}: {1}'.format(x, y))
