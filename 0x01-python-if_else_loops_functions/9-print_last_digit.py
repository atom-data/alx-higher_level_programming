#!/usr/bin/python3
def print_last_digit(number):
    """Prints and returns the last digit of a number"""
    if number < 0:
        number = -1 * number

    last_digit = number % 10
    print(last_digit, end='')
    return last_digit
