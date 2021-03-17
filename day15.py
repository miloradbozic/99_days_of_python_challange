'''
Return an array whose values are indexes of the first array in order to get the asked word
'''


def solution(letter_pairs, word):
    word = word.lower()
    hash = dict()
    for i in range(len(letter_pairs)):
        hash[letter_pairs[i].lower()] = i

    res = []
    for i in range(int(len(word) / 2)):
        c = word[i*2: i*2+2]
        res.append(hash.get(c))

    return res


assert solution(["RI", "CA", "MA"], "Marica") == [2, 0, 1]
assert solution(["MA", "DA"], "Mada") ==  [0, 1]

