#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    for item in range(x):
        if isinstance(my_list[item], int):
            try:
                print(my_list[item], end='')
            except IndexError:
                break
        else:
            continue
        i += 1
    print()
    return i
