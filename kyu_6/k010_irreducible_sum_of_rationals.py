"""
Irreducible Sum of Rationals

You will have a list of rationals in the form

lst = [ [numer_1, denom_1] , ... , [numer_n, denom_n] ]
or

lst = [ (numer_1, denom_1) , ... , (numer_n, denom_n) ]
where all numbers are positive integers. You have to produce their sum N / D in an irreducible form: this means
that N and D have only 1 as a common divisor.

Example:
[ [1, 2], [1, 3], [1, 4] ]  -->  [13, 12]
1/2  +  1/3  +  1/4     =      13/12
Note
See sample tests for more examples and form of results.
"""
from fractions import Fraction


def sum_fracts(lst):
    if not lst:
        return None

    result = sum(Fraction(n, d) for n, d in lst)
    if result.denominator == 1:
        return result.numerator

    return [result.numerator, result.denominator]


assert sum_fracts([[1, 2], [1, 3], [1, 4]]) == [13, 12]
assert sum_fracts([[1, 3], [5, 3]]) == 2
assert sum_fracts([[12, 3], [15, 3]]) == 9
assert sum_fracts([[2, 7], [1, 3], [1, 12]]) == [59, 84]
assert sum_fracts([]) is None
