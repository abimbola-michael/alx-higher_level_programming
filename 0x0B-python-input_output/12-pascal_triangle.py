#!/usr/bin/python3
"""function that returns a list of lists of integers
representing the Pascal’s triangle of n"""


def pascal_triangle(n):
    """ pascal triangle"""

    if n <= 0:
        return []
    trgls = [[1]]

    while len(trgls) != n:
        trgl = trgls[-1]
        temp_trgl = [1]
        for i in range(len(trgl) - 1):
            temp_trgl.append(trgl[i] + trgl[i + 1])
            temp_trgl.append(1)
        trgls.append(temp_trgl)
    return trgls
