"""
A method for converting a string representing a binary number to it's decimal representation
"""


def decimal_to_binary(number):
    base = 2
    exp = 0
    sum = 0
    for n in number[::-1]:
        sum += int(n) * base ** exp
        exp += 1
    return sum


assert decimal_to_binary("1011") == 11
assert decimal_to_binary("10") == 2
assert decimal_to_binary("0") == 0
