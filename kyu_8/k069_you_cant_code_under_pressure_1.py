"""
You Can't Code Under Pressure #1

Code as fast as you can! You need to double the integer and return it.
"""


def double_integer(i):
    return i << 1


assert double_integer(2) == 4
assert double_integer(4) == 8
assert double_integer(-10) == -20
assert double_integer(0) == 0
assert double_integer(100) == 200
