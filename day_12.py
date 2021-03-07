"""
Write a function which checks if an array is a permutation
"""


def is_permutation(A):
    values = [False] * len(A)

    for v in A:
        i = v-1
        if i > len(A) - 1:
            return 0
        values[v-1] = True

    for v in values:
        if not v:
            return 0

    return 1


assert is_permutation([4, 1, 3, 2]) == 1
assert is_permutation([4, 1, 3]) == 0
assert is_permutation([1]) == 1
assert is_permutation([1, 7, 4, 3]) == 0
assert is_permutation([1, 7, 4, 3, 2, 5, 6]) == 1

