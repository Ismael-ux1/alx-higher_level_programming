#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div
    import sys
    """
    Calculate and print the result of an arithmetic operation.
    """
    if len(sys.argv) != 4:
        print("Usage:./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    oop = {"+": add, "-": sub, "*": mul, "/": div}
    if sys.argv[2] not in list(oop.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, sys.argv[2], b, oop[sys.argv[2]](a, b)))
