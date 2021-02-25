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


def factorial(N):
    factorial = 1
    for i in range(1, N+1):
        factorial *= i
    return factorial


assert factorial(1) == 1
assert factorial(2) == 2
assert factorial(5) == 120
assert factorial(6) == 720


def triangle(N):
    for i in range(1, N+1):
        for j in range(i):
            print('*', end="")
        print('')


def symmetric_triangle(N):
    res = ""
    for i in range(N):
        for j in range(i):

            res += ' '
        for k in range(N*2-1 - i*2):
            res += '*'
        res += '\n'
    return res


assert symmetric_triangle(6) == """***********
 *********
  *******
   *****
    ***
     *
"""
