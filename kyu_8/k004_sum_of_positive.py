"""
Sum of positive

Task
You get an array of numbers, return the sum of all of the positives ones.

Example
[1, -4, 7, 12] => 1 + 7 + 12 = 20
Note
If there is nothing to sum, the sum is default to 0.
"""


def positive_sum(arr):
    return sum(x for x in arr if x > 0)


assert positive_sum([1, 2, 3, 4, 5]) == 15
assert positive_sum([1, -2, 3, 4, 5]) == 13
assert positive_sum([-1, 2, 3, 4, -5]) == 9
assert positive_sum([]) == 0
assert positive_sum([-1, -2, -3, -4, -5]) == 0
