"""
A method for converting a string representing decimal number to a binary representation of a number as a string
- use floor division by 2 method
"""

# Algorithm explained here: https://indepth.dev/posts/1019/the-simple-math-behind-decimal-binary-conversion-algorithms
def decimal_to_binary(number):
    if number == 0:
        return "0"

    res = []
    while number != 0:
        res.append(number % 2)
        number = number // 2

    final_res = ""
    while len(res) > 0:
        final_res += str(res.pop())

    return final_res


assert decimal_to_binary(9) == "1001"
assert decimal_to_binary(11) == "1011"
assert decimal_to_binary(2) == "10"
assert decimal_to_binary(0) == "0"
assert decimal_to_binary(3819) == "111011101011"
assert decimal_to_binary(798340) == "11000010111010000100"
