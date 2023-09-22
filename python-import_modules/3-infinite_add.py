#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    value = 0
    for sum in range(len(sys.argv)-1):
        value += int(sys.argv[sum + 1])
    print("{}".format(value))
