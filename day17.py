'''
Implement selection sort algorithm
'''


def selection_sort(A):
    for i in range(len(A)):
        for j in range(i, len(A)):
            if A[j] < A[i]:
                A[j], A[i] = A[i], A[j]
    return A


assert selection_sort([4,1,6,2,3]) == [1,2,3,4,6]
assert selection_sort([1,6,2,3,5]) == [1,2,3,5,6]
assert selection_sort([]) == []
assert selection_sort([3]) == [3]

'''
Implement counting sort algorithm, range of values is (0,1000000)
'''


def count_sort(A):
    count = [0] * 1000000
    for v in A:
        count[v] +=1

    res = []
    for i in range(len(count)):
        for j in range(count[i]):
            res.append(i)

    return res


assert count_sort([4,1,6,2,3]) == [1,2,3,4,6]
assert count_sort([1,6,2,3,5]) == [1,2,3,5,6]
assert count_sort([]) == []
assert count_sort([3]) == [3]