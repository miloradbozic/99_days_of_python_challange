'''
GenomicRangeQuery - Find the minimal nucleotide from a range of sequence DNA.
'''
import cProfile


def solution(S, P, Q):
    char_dict = {"A": 1, "C": 2, "G": 3, "T":4 }
    # value_S = []
    # for c in S:
    #     value_S.append(char_dict[c])

    V = [0] * len(P)
    for i in range(len(P)):
        start_index = P[i]
        end_index = Q[i]
        smallest = 4
        for j in range(start_index, end_index+1):
            letter = S[j]
            if char_dict[letter] < smallest:
                smallest = char_dict[letter]
        V[i] = smallest

    return V


print(solution("CAGCCTA", [2, 5, 0], [4, 5, 6]))