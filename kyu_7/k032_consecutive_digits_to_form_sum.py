"""
Consecutive Digits To Form Sum

Positive integers have so many gorgeous features. Some of them could be expressed as a sum of two or more consecutive
positive numbers.

Consider an Example :
10 could be expressed as the sum of 1 + 2 + 3 + 4 .
Task
Given Positive integer, N , return true if it could be expressed as a sum of two or more consecutive positive numbers ,
otherwise return false .

Notes
Guaranteed constraint : 2 ≤ N ≤ (2^32) -1 .
Input >> Output Examples:

* consecutiveDucks(9)  ==>  return (true)  //  9 , could be expressed as a sum of ( 2 + 3 + 4 ) or ( 4 + 5 ) .

* consecutiveDucks(64)  ==>  return (false)

* consecutiveDucks(42)  ==>  return (true) //  42 , could be expressed as a sum of ( 9 + 10 + 11 + 12 )  .
"""


# Conclusion: A number can be represented as the sum of two or more consecutive natural numbers
# if and only if it is NOT a power of two.

def consecutive_ducks(n: int) -> bool:
    # If n is a power of two, return False, otherwise True.
    return (n & (n - 1)) != 0


from math import log2


def consecutive_ducks2(n):
    return not log2(n).is_integer()


assert consecutive_ducks(69) == True
assert consecutive_ducks(8) == False
assert consecutive_ducks(57) == True
assert consecutive_ducks(6) == True
assert consecutive_ducks(13) == True
assert consecutive_ducks(16) == False
assert consecutive_ducks(91) == True
assert consecutive_ducks(75) == True
assert consecutive_ducks(38) == True
assert consecutive_ducks(25) == True
assert consecutive_ducks(32) == False
assert consecutive_ducks(65) == True
assert consecutive_ducks(13) == True
assert consecutive_ducks(16) == False
assert consecutive_ducks(99) == True

assert consecutive_ducks(522) == True
assert consecutive_ducks(974) == True
assert consecutive_ducks(755) == True
assert consecutive_ducks(512) == False
assert consecutive_ducks(739) == True
assert consecutive_ducks(1006) == True
assert consecutive_ducks(838) == True
assert consecutive_ducks(1092) == True
assert consecutive_ducks(727) == True
assert consecutive_ducks(648) == True
assert consecutive_ducks(1024) == False
assert consecutive_ducks(851) == True
assert consecutive_ducks(541) == True
assert consecutive_ducks(1011) == True
assert consecutive_ducks(822) == True

assert consecutive_ducks(382131) == True
assert consecutive_ducks(118070) == True
assert consecutive_ducks(17209) == True
assert consecutive_ducks(32768) == False
assert consecutive_ducks(161997) == True
assert consecutive_ducks(400779) == True
assert consecutive_ducks(198331) == True
assert consecutive_ducks(325482) == True
assert consecutive_ducks(88441) == True
assert consecutive_ducks(648) == True
assert consecutive_ducks(65536) == False
assert consecutive_ducks(323744) == True
assert consecutive_ducks(183540) == True
assert consecutive_ducks(65271) == True
assert consecutive_ducks(5263987) == True
