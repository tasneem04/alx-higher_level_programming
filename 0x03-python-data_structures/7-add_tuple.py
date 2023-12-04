#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_a = list(tuple_a)
    list_b = list(tuple_b)
    print(len(list_a))
    for idx in range(0, (len(list_a)-1)):
        if list_a[idx] == "":
            list_a[idx] = 0
            print("the list idx {} is  {}".fomrat(idx,list_a[idx]))
            tuple_a = tuple(list_a)
        else:
            continue
    for ind in range(0, (len(tuple_b)-1)):
        if list_b[ind] == '':
            list_b[ind] = 0
            tuple_b = tuple(list_b)
        else:
            continue
    result = tuple(map(sum, zip(tuple_a, tuple_b)))
    return result
