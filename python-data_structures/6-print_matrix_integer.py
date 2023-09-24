#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for items in matrix:
            i = 1
            length = len(items)
            for elems in items:
                if i == length:
                    print('{:d}'.format(elems), end='')
                else:
                    print('{:d}'.format(elems), end=' ')
                i += 1
            print()
