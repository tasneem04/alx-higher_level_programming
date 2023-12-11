#!/usr/bin/python3
def remove_char_at(str, n):
    cp_str = list(str)
    for i in range(0, (len(str)-1)):
        if i == n:
            del cp_str[i]
            return "".join(cp_str)
        else:
            return "".join(cp_str)

