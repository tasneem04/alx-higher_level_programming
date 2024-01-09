#!/usr/bin/python3
"""Module containing the function read_file"""


def read_file(filename=""):
    """reads text file"""
    with open(filename, mode='r', encoding='utf-8') as a_file:
        print(a_file.read(), end='')
        a_file.close()
