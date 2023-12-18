#!/usr/bin/python3
def safe_print_integer(value):
    if isinstance(value, int):
        try:
            print("{:d}".format(value))
        except(ValueError, TypeError):
            return False
        else:
            return True
