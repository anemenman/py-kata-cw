"""
Find the odd int

Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""
from functools import reduce
from operator import xor


# XOR provides commutativity and associativity, so the order does not matter - all pairs will "cancel out" and only the
# desired number will follow.
def find_it(arr):
    result = 0
    for num in arr:
        result ^= num
    return result


def find_it_v2(arr):
    return reduce(xor, arr)


assert find_it([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]) == 5
assert find_it([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) == -1
assert find_it([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) == 5
assert find_it([10]) == 10
assert find_it([10, 10, 10]) == 10
assert find_it([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]) == 10
assert find_it([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]) == 1

assert find_it_v2([20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]) == 5
assert find_it_v2([1, 1, 2, -2, 5, 2, 4, 4, -1, -2, 5]) == -1
assert find_it_v2([20, 1, 1, 2, 2, 3, 3, 5, 5, 4, 20, 4, 5]) == 5
assert find_it_v2([10]) == 10
assert find_it_v2([10, 10, 10]) == 10
assert find_it_v2([1, 1, 1, 1, 1, 1, 10, 1, 1, 1, 1]) == 10
assert find_it_v2([5, 4, 3, 2, 1, 5, 4, 3, 2, 10, 10]) == 1
