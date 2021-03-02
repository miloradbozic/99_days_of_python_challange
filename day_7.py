"""
3-time_complexity/tape_equilibrium

Find a missing element in an array of consecutive elements
"""

def find_missing(A):
    max_elem = len(A) + 1
    pair_sum = max_elem + 1

    table = set()
    if max_elem % 2 == 1:
        table.add(int(pair_sum / 2))

    for elem in A:
        opposite = pair_sum - elem
        if opposite in table:
            table.remove(opposite)
        else:
            table.add(elem)

    return pair_sum - next(iter(table))

assert find_missing([2,4,1,5]) == 3
assert find_missing([2,4,3,5]) == 1
assert find_missing([1]) == 2
assert find_missing([2]) == 1

"""
Find a minimum absolute difference between two parts of an array
"""
# todo repeat
def find_minimum_dif(A):
    total_sum = 0
    for val in A:
        total_sum += val

    min_diff = None
    p1_sum = 0
    for val in A[0:len(A)-1]:
        p1_sum += val
        p2_sum = total_sum - p1_sum
        current_min_diff = abs(p1_sum - p2_sum)
        if min_diff == None or current_min_diff < min_diff:
            min_diff = current_min_diff

    return min_diff


print(find_minimum_dif([-1,1]))