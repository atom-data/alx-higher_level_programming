#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    for index, argument in enumerate(sys.argv):
        if index > 0:
            sum += int(argument)
    print(sum)
