#!/usr/bin/python3
def search_replace(my_list, search, replace):
    cp_list = my_list.copy()
    for idx, item in enumerate(cp_list):
        if item == search:
            cp_list[idx] = replace

    return cp_list
