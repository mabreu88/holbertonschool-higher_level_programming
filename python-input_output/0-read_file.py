#!/usr/bin/python3
""" function that reads a text file (UTF8) and prints it to stdout """


def read_file(filename=""):
    """ Block that read a file and print the content """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")