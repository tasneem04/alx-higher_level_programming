#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for idx in a_dictionary:
        new_dictionary[idx] = a_dictionary[idx] * 2
    return new_dictionary
