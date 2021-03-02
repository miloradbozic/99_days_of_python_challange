"""
Given array A consisting of N integers, return the reversed array.
"""
import cProfile


def reverse_array1(array):
    res = []
    i = len(array)
    while i > 0:
        res.append(array[i - 1])
        i -= 1
    return res


def reverse_array2(array):
    N = len(array)
    for i in range(N // 2):
        tmp = array[i]
        array[i] = array[N - i - 1]
        array[N - i - 1] = tmp

    return array


p = cProfile.Profile()
p.runcall(reverse_array1, list(range(100)))
p.print_stats()
p = cProfile.Profile()
p.runcall(reverse_array2, list(range(100)))
p.print_stats()


def rotate(A, K):
    if len(A) == 0:
        return []

    K = K % len(A)

    for j in range(K):
        prev_index = len(A) - 1
        prev_elem = A[prev_index]
        for i in range(len(A)):
            tmp = A[i]
            A[i] = prev_elem
            prev_elem = tmp

    return A


assert rotate([1, 2, 3, 4], 9) == [4, 1, 2, 3]
