"""
Count of positives / sum of negatives

Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative
numbers. 0 is neither positive nor negative.
If the input is an empty array or is null, return an empty array.

Example
For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].
"""


def count_positives_sum_negatives(arr):
    if not arr:
        return []

    pos_count = 0
    neg_sum = 0

    for num in arr:
        if num > 0:
            pos_count += 1
        elif num < 0:
            neg_sum += num

    return [pos_count, neg_sum]


assert count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]) == [10, -65]
assert count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]) == [8, -50]
assert count_positives_sum_negatives([1]) == [1, 0]
assert count_positives_sum_negatives([-1]) == [0, -1]
assert count_positives_sum_negatives([0, 0, 0, 0, 0, 0, 0, 0, 0]) == [0, 0]
assert count_positives_sum_negatives([]) == []
