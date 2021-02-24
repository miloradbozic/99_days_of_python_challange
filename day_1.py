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

# More simple algorithm explained here: https://indepth.dev/posts/1019/the-simple-math-behind-decimal-binary-conversion-algorithms
def decimal_to_binary2(number):
    sum = 0
    for n in number[:]:
        sum = 2 * sum + int(n)

    return sum


assert decimal_to_binary("1011") == 11
assert decimal_to_binary("10") == 2
assert decimal_to_binary("0") == 0

assert decimal_to_binary2("1011") == 11
assert decimal_to_binary2("10") == 2
assert decimal_to_binary2("0") == 0
