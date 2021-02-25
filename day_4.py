"""
A method for finding the longest binary gap of a number
"""


def longest_binary_gap(number):
    gap = 0
    longest_gap = 0
    start_gap = False
    while number > 0:
        if number % 2 == 0:
            if start_gap:
                gap += 1
        else:
            start_gap = True

            if gap > longest_gap:
                longest_gap = gap
            gap = 0

        number = number // 2

    return longest_gap


assert longest_binary_gap(9) == 2
assert longest_binary_gap(529) == 4
assert longest_binary_gap(20) == 1
assert longest_binary_gap(15) == 0
assert longest_binary_gap(0) == 0
