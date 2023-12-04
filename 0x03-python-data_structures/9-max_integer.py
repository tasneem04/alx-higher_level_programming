#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) != 0:
        for i in range(0, (len(my_list)-1)):
            for j in range(0 ,(len(my_list)-1)):
                if my_list[i] >=  my_list[j+1]:
                    return my_list[i]
                else:
                    return my_list[j+1]
    else:
        return None
        
