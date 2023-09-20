#!/usr/bin/python3
def uppercase(str):
    for char in str:
        char = ord(char)
        if char > 96 and char < 123:
            char -= 32
        print("{}".format(chr(char)), end="")
    print()
