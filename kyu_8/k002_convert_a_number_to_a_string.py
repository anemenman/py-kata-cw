"""
Convert a Number to a String!

We need a function that can transform a number (integer) into a string.

What ways of achieving this do you know?

Examples (input --> output):
123  --> "123"
999  --> "999"
-100 --> "-100"
"""


def number_to_string(num):
    return str(num)


assert number_to_string(67) == '67'
assert number_to_string(79585) == '79585'
assert number_to_string(-79585) == '-79585'
assert number_to_string(1 + 2) == '3'
assert number_to_string(1 - 2) == '-1'
assert number_to_string(0) == '0'
