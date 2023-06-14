#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    left, right = 0, 0

    for item in my_list:
        left += (item[0] * item[1])
        right += item[1]
        return (left / right)
