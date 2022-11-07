#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    number = len(sys.argv) - 1
    if number != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    operator = sys.argv[2]
    if operator == '+':
        operation = add
    elif operator == '-':
        operation = sub
    elif operator == '*':
        operation = mul
    elif operator == '/':
        operation = div
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    result = int(operation(a, b))
    print("{:d} {:s} {:d} = {:d}".format(a, operator, b, result))
