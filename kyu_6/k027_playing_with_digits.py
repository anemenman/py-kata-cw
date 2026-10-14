"""
Playing with digits

Some numbers have funny properties. For example:

89 --> 8¹ + 9² = 89 * 1
695 --> 6² + 9³ + 5⁴= 1390 = 695 * 2
46288 --> 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
Given two positive integers n and p, we want to find a positive integer k, if it exists, such that the sum of the
digits of n raised to consecutive powers starting from p is equal to k * n.

If it is the case we will return k, if not return -1.

Note: n and p will always be strictly positive integers.

Examples:
n = 89; p = 1 ---> 1 since 8¹ + 9² = 89 = 89 * 1

n = 92; p = 1 ---> -1 since there is no k such that 9¹ + 2² equals 92 * k

n = 695; p = 2 ---> 2 since 6² + 9³ + 5⁴= 1390 = 695 * 2

n = 46288; p = 3 ---> 51 since 4³ + 6⁴+ 2⁵ + 8⁶ + 8⁷ = 2360688 = 46288 * 51
"""


def dig_pow(n, p):
    digits = str(n)
    total = sum(int(d) ** (p + i) for i, d in enumerate(digits))

    if total % n == 0:
        return total // n
    return -1


assert dig_pow(89, 1) == 1
assert dig_pow(92, 1) == -1
assert dig_pow(46288, 3) == 51
assert dig_pow(41, 5) == 25
assert dig_pow(114, 3) == 9
assert dig_pow(8, 3) == 64
