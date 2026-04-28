"""
Remove duplicates from list

Define a function that removes duplicates from an array of non negative numbers and returns it as a result.
The order of the sequence has to stay the same.
Examples:
Input -> Output
[1, 1, 2] -> [1, 2]
[1, 2, 1, 1, 3, 2] -> [1, 2, 3]
"""
from collections import OrderedDict


def distinct(arr):
    return list(dict.fromkeys(arr))
    # return list(OrderedDict.fromkeys(arr))  # for Python < 3.7


assert distinct([1]) == [1]
assert distinct([1, 2]) == [1, 2]
assert distinct([1, 1, 2]) == [1, 2]
assert distinct([1, 1, 1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
assert distinct([1, 2, 2, 3, 3, 4, 4, 5, 6, 7, 7, 7]) == [1, 2, 3, 4, 5, 6, 7]
