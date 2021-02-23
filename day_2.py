"""
A method for converting a string representing decimal number to a binary representation of a number as a string
"""


def decimal_to_binary(number):
    if number == 0:
        return "0"

    exp = 0
    while number >= 2 ** exp:
        exp += 1

    res = ""
    while exp > 0:
        exp = exp - 1
        if number / 2 ** exp >= 1:
            res += "1"
            number = number - 2 ** exp
        else:
            res += "0"

    return res


assert decimal_to_binary(9) == "1001"
assert decimal_to_binary(11) == "1011"
assert decimal_to_binary(2) == "10"
assert decimal_to_binary(0) == "0"
assert decimal_to_binary(3819) == "111011101011"
assert decimal_to_binary(798340) == "11000010111010000100"
