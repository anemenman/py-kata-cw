"""
Sum Arrays

Write a function that takes an array of numbers and returns the sum of the numbers. The numbers can be negative. If the
array is empty, return 0.

Examples
Input: [1, 5.2, 4, 0, -1]
Output: 9.2

Input: [-2.398]
Output: -2.398

Input: []
Output: 0
"""


def sum_array(numbers: list) -> float:
    return sum(numbers)


assert sum_array([]) == 0
assert sum_array([1, 2, 3]) == 6
assert sum_array([1.1, 2.2, 3.3]) == 6.6
assert sum_array([4, 5, 6]) == 15
assert sum_array(range(101)) == 5050
