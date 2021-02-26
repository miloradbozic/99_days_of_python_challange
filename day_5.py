"""
Given array A consisting of N integers, return the reversed array.
"""
import cProfile


def reverse_array1(array):
    res = []
    i = len(array)
    while i > 0:
        res.append(array[i-1])
        i -= 1
    return res

def reverse_array2(array):
    N = len(array)
    for i in range(N//2):
        tmp = array[i]
        array[i] = array[N-i-1]
        array[N-i-1] = tmp

    return array


p = cProfile.Profile()
p.runcall(reverse_array1, list(range(10000000)))
p.print_stats()
p = cProfile.Profile()
p.runcall(reverse_array2, list(range(10000000)))
p.print_stats()