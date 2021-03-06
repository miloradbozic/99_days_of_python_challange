"""
Write a function that, given an array A of N integers,
returns the smallest positive integer (greater than 0) that does not occur in A.
"""

# O(n^2)
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


# O(n) + O(m)
def get_smallest_positive2(A):
    values = [False] * 100000
    for v in A:
        values[v-1] = True

    for i in range(len(values)):
        if not values[i]:
            return i+1


assert get_smallest_positive2([1, 3, 6, 4, 1, 2]) == 5
assert get_smallest_positive2([-2, -1]) == 1