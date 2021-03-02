"""
A non-empty array A consisting of N integers is given.
The array contains an odd number of elements, and each
element of the array can be paired with another element
that has the same value, except for one element that is
left unpaired.
"""
import cProfile
from math import ceil


def get_unpaired(A):
    value_set = set()
    for elem in A:
        if elem in value_set:
            value_set.remove(elem)
        else:
            value_set.add(elem)
    return value_set.pop()


assert get_unpaired([9,3,9]) == 3


def solution(X, Y, D):
    return ceil((Y-X)/D)


print(solution(1, 100, 1))
