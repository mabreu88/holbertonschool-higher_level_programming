#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arguments = len(sys.argv) - 1
    if arguments == 0:
        print("0 arguments.")
    elif arguments == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arguments))
    for a in range(1, arguments + 1):
        print("{}: {}".format(a, sys.argv[a]))
