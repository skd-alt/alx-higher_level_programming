#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    is_divisible = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            is_divisible.append(True)
        else:
            is_divisible.append(False)

    return (is_divisible)
