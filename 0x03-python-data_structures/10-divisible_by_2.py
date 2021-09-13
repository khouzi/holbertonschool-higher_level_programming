#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    New_L = []
    for i in my_list:
        if my_list[i] % 2 == 0:
            New_L.append(True)
        else:
            New_L.append(False)
    return New_L
