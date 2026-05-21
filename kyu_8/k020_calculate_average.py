"""
Calculate average

Write a function which calculates the average of the numbers in a given array.
Note: Empty arrays should return 0.
"""


def find_average(numbers: list[int]) -> float:
    return sum(numbers) / len(numbers) if numbers else 0


assert find_average([1, 2, 3]) == 2
assert find_average([]) == 0
assert find_average([1, 2]) == 1.5
