#!/usr/bin/python3

def print_last_digit(number):
    abs_number = abs(number)
    last_number = abs_number % 10
    print(last_number, end='')
    return last_number
