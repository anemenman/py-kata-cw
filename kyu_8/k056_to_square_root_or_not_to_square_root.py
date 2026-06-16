"""
To square(root) or not to square(root)

Write a method, that will get an integer array as parameter and will process every number from this array.
Return a new array with processing every number of the input-array like this:
If the number has an integer square root, take this, otherwise square the number.

Example
[4,3,9,7,2,1] -> [2,9,3,49,4,1]
Notes
The input array will always contain only positive numbers, and will never be empty or null.
"""
import math


def square_or_square_root(arr):
    return [math.isqrt(n) if math.isqrt(n) ** 2 == n else n ** 2 for n in arr]


assert square_or_square_root([4, 3, 9, 7, 2, 1]) == [2, 9, 3, 49, 4, 1]
assert square_or_square_root([100, 101, 5, 5, 1, 1]) == [10, 10201, 25, 25, 1, 1]
assert square_or_square_root([1, 2, 3, 4, 5, 6]) == [1, 4, 9, 2, 25, 36]
