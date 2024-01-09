#!/usr/bin/python3
"""Module containing the function write_file"""


def number_of_lines(filename=""):
    """returns number of lines in a file"""
    lines = 0
    with open(filename, mode='r', encoding='utf-8') as a_file:
        for i, l in enumerate(a_file):
            lines += 1
    return lines
