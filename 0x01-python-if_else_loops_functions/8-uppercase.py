#!/usr/bin/python3
def uppercase(str):
    """Print string in uppercase characters"""
    for a in str:
        c = ord(a)
        if c >= 97 and c <= 122:
            c = c - 32

        char = chr(c)
        print("{:s}".format(char), end='')

    print()
