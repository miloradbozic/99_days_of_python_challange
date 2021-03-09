'''
This array represents number of mushrooms growing on the
consecutive spots along a road. A mushroom picker is at
spot number k on the road and should perform m moves.
Calculate the maximum number of mushrooms that the mushroom
 picker can collect in m moves.
'''

def get_prefix_sums(A):
    sums = [0] * (len(A) + 1)
    for i in range(1, len(A)+1):
        sums[i] = sums[i-1] + A[i-1]

    return sums

# log(nm)
def find_maximum(A,k, m):
    max_sum = 0
    for i in range(m+1):
        sum = A[k]
        for j in range(1, i+1):
            index = k - j
            if index < 0:
                continue
            sum += A[k-j]
        for j in range(1, m - 2*i + 1):
            index = k + j
            if index > len(A) - 1:
                continue
            sum += A[k+j]
        max_sum = max(max_sum, sum)

    return max_sum


def find_maximum2(A,k, m):
    prefix_sums = get_prefix_sums(A)
    max_sum = 0
    for i in range(max(k, m+1)):
        sum = A[k]
        min_index = k-i
        left_sum = prefix_sums[k] - prefix_sums[min_index]

        max_index = min(len(A)-1, k + m-2*i)
        if max_index > k:
            right_sum = prefix_sums[max_index+1] - prefix_sums[k+1]
        else:
            right_sum = 0

        sum += left_sum + right_sum
        max_sum = max(max_sum, sum)

    return max_sum

assert find_maximum2([2, 3, 7, 5, 1, 3, 9], 4, 6) == 25
assert find_maximum2([2, 3, 9], 1, 2) == 12
assert find_maximum2([9], 0, 1) == 9


