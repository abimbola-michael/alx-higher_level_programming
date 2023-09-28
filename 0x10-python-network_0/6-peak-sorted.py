#!/usr/bin/python3
"""a function that finds a peak in a list of unsorted integers."""

def find_peak(list_of_integers):
    """finds a peak in a list of unsorted integers"""

    if not list_of_integers or len(list_of_integers) < 1:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    return sortList(list_of_integers)[0]

def sortList(list_of_integers):
    """function to sort list with merge sort algorithm"""
    if len(list_of_integers) <= 1:
        return list_of_integers
    mid = len(list_of_integers) // 2
    left = sortList(list_of_integers[:mid])
    right = sortList(list_of_integers[mid:])
    i = j = 0
    sortedList = []
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            sortedList.append(left[i])
            i += 1
        else:
            sortedList.append(right[j])
            j += 1

    while i < len(left):
        sortedList.append(left[i])
        i += 1
    while j < len(right):
        sortedList.append(right[j])
        j += 1
    return sortedList
