#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    number = len(sys.argv) - 1
    if number == 1:
        label = 'argument'
    else:
        label = 'arguments'
    if number == 0:
        terminator = '.'
    else:
        terminator = ':'
    print("{:d} {:s}{:s}".format(number, label, terminator))
    for index, argument in enumerate(sys.argv):
        if index > 0:
            print("{}: {}".format(index, argument))
