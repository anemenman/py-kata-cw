"""
Beginner - Lost Without a Map

Given an array of integers, return a new array with each value doubled.
For example:

[1, 2, 3] --> [2, 4, 6]
"""


def maps(arr: list[int]) -> list[int]:
    return [x * 2 for x in arr]


assert maps([1, 2, 3]) == [2, 4, 6]
assert maps([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) == [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
assert maps([]) == []
