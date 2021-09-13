#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    else:
        k = my_list[0]
        for i in my_list:
            if k < my_list[i]:
                k = my_list[i]
        return k
