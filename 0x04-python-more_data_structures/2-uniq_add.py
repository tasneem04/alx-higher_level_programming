#!/usr/bin/python3
def uniq_add(my_list=[]):
    cp_list = list(set(my_list))
    result = 0

    for num in cp_list:
        result += num
    return result
