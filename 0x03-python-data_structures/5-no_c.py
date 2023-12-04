#!/usr/bin/python3
def no_c(my_string):
    if not my_string:
        return None
    cp_list = []
    for i in range(0, len(my_string)):
        cp_list.append(my_string[i])
    for i in range(0, len(my_string)):
        if cp_list[i] == 'c' or cp_list[i] == 'C':
            del cp_list[i]
            cp_list = "".join(map(str, cp_list))
            return str(cp_list)
