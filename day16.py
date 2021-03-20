'''
PassingCars
'''

def solution(A):
    prefix_sums = get_prefix_sums(A)
    passing_cars_sum = 0
    for i in range(len(A)):
        if A[i] == 0:
            passing_cars_sum += prefix_sums[len(A)] - prefix_sums[i]
            if passing_cars_sum > 1000000000:
                return -1

    return passing_cars_sum

def get_prefix_sums(A):
    K = [0] * (len(A) + 1)
    for i in range(len(A)):
        K[i+1] = K[i] + A[i]
    return K


solution([0, 1, 0, 1, 1]) == 5

