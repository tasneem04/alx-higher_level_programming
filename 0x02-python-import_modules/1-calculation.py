#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import a, b, add, sub, mul, div
    print("{} + {} = {}".format(a, b, add(a, b)), end='\n')
    print("{} - {} = {}".format(a, b, sub(a, b)), end='\n')
    print("{} * {} = {}".format(a, b, mul(a, b)), end='\n')
    print("{} / {} = {}".format(a, b, div(a, b)), end='\n')
