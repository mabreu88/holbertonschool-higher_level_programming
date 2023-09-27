#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    print_counter = 0
    for i in range(x):
        try:
            if type(my_list[i]) is int and print_counter != x:
                print('{:d}'.format(my_list[i]), end='')
                print_counter += 1
        except TypeError:
            continue
    print()
    return print_counter
