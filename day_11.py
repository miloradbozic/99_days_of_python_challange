"""
Write a function that, given an array A of N integers,
returns the smallest positive integer (greater than 0) that does not occur in A.
"""

def get_smallest_positive(A):
    smallest = 1
    i = 0
    while i < len(A):
        if A[i] == smallest:
            smallest += 1
            i = 0
        else:
            i += 1

    return smallest


assert get_smallest_positive([1, 3, 6, 4, 1, 2]) == 5
assert get_smallest_positive([-2, -1]) == 1