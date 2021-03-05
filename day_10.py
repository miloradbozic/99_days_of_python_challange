"""
MaxCounters - N is the number of counters, A is the array which represents operations where
if A[K] = X, such that 1 ≤ X ≤ N, then operation K is increase(X),
if A[K] = N + 1 then operation K is max counter.
Return the resulting value of all counters.
"""

def max_counters(N, A):
    counters = [0] * N
    max_elem = 0
    floor = 0
    for v in A:
        if v <= N:
            counters[v-1] = max(counters[v-1], floor) + 1
            max_elem = max(max_elem, counters[v-1])
        else:
            floor = max_elem

    for i in range(len(counters)):
        if counters[i] < floor:
            counters[i] = floor

    return counters


print(max_counters(5, [1,1,6,2]))
