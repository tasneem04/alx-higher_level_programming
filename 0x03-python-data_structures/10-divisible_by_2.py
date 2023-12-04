#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    cp_list = []
    for i in my_list:
        if (my_list[i] % 2) == 0:
            cp_list.append(True)
        else:
            cp_list.append(False)
    return cp_list
