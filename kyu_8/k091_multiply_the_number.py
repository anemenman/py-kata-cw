"""
Multiply the number

Jack really likes his number five: the trick here is that you have to multiply each number by 5 raised to the number of
digits of each numbers, so, for example:

  3 -->    15  (  3 * 5¹)
 10 -->   250  ( 10 * 5²)
200 --> 25000  (200 * 5³)
  0 -->     0  (  0 * 5¹)
 -3 -->   -15  ( -3 * 5¹)
"""


def multiply(n):
    return n * 5 ** len(str(abs(n)))


assert multiply(10) == 250
assert multiply(5) == 25
assert multiply(200) == 25000
assert multiply(0) == 0
assert multiply(-2) == -10
