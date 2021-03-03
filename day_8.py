"""
Having two arrays of N elements, count if there is swap operation such as that
sum of elements of both arrays after the swap is the same.
"""

def swap(A, B):
    sum_a = 0
    sum_b = 0
    for v in A:
        sum_a+=v
    for v in B:
        sum_b+=v

    for i in range(len(A)):
        tmp = A[i]
        for j in range(len(B)):
            sum_a_now = sum_a - tmp + B[j]
            sum_b_now = sum_b - B[j] + tmp
            if sum_a_now == sum_b_now:
                return True, i, j

    return False


def swap_v2(A, B):
    sum_a = 0
    sum_b = 0
    for v in A:
        sum_a+=v
    for v in B:
        sum_b+=v

    if sum_b % sum_a == 1:
        return False

    map = dict()
    for i in range(len(A)):
        map[sum_b - sum_a + 2*A[i]] = i

    for j in range(len(B)):
        searched_key = 2 * j
        if searched_key in map.keys():
            return True, map[searched_key], j

    return False


assert swap([1,2,3], [3,3,2]) == swap_v2([1,2,3], [3,3,2]) == (True, 0, 2)