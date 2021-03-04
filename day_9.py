"""
Having a frog jumping on leaves, where array A represents an array whose elements represent positions
where the individual leaves fall at second given by the array element index, and X+1 is place where frog needs to jump,
calculate the earliest position in time
"""

def frog_jump(X, A):
    leaf_count = 0
    leaves = [False] * X
    print(leaves)
    for i in range(len(A)):
        if leaves[A[i]-1] == False:
            leaves[A[i]-1] = True
            leaf_count+=1
            if leaf_count == X:
                return i
    return -1



assert swap([1,2,3], [3,3,2]) == swap_v2([1,2,3], [3,3,2]) == (True, 0, 2)