"""
Odd/Even number of divisors

Given an integer n return "odd" if the number of its divisors is odd. Otherwise return "even".

Note: big inputs will be tested.

Examples:
All prime numbers have exactly two divisors (hence "even").

For n = 12 the divisors are [1, 2, 3, 4, 6, 12] – "even".

For n = 4 the divisors are [1, 2, 4] – "odd".
"""
import math


# the number of divisors is odd and only if the number is an exact square (perfect square).
def oddity(n):
    root = math.isqrt(n)

    if root * root == n:
        return 'odd'
    else:
        return 'even'


assert oddity(1) == 'odd'
assert oddity(5) == 'even'
assert oddity(16) == 'odd'
