"""
Find Maximum and Minimum Values of a List

Your task is to make two functions ( max and min, or maximum and minimum, etc., depending on the language ) that
receive a list of integers as input, and return the largest and lowest number in that list, respectively. Each function
returns one number.

Examples (Input -> Output)
* [4,6,2,1,9,63,-134,566]         -> max = 566, min = -134
* [-52, 56, 30, 29, -54, 0, -110] -> min = -110, max = 56
* [42, 54, 65, 87, 0]             -> min = 0, max = 87
* [5]                             -> min = 5, max = 5
Notes
You may consider that there will not be any empty arrays/vectors.
"""


def get_min(arr: list[int]) -> int:
    return min(arr)


def get_max(arr: list[int]) -> int:
    return max(arr)


def minimum(arr: list[int]) -> int:
    current_min = arr[0]
    for num in arr:
        if num < current_min:
            current_min = num
    return current_min


def maximum(arr: list[int]) -> int:
    current_max = arr[0]
    for num in arr:
        if num > current_max:
            current_max = num
    return current_max


assert minimum([-52, 56, 30, 29, -54, 0, -110]) == -110
assert minimum([42, 54, 65, 87, 0]) == 0
assert minimum([1, 2, 3, 4, 5, 10]) == 1
assert minimum([-1, -2, -3, -4, -5, -10]) == -10
assert minimum([9]) == 9

assert maximum([-52, 56, 30, 29, -54, 0, -110]) == 56
assert maximum([4, 6, 2, 1, 9, 63, -134, 566]) == 566
assert maximum([5]) == 5
assert maximum([534, 43, 2, 1, 3, 4, 5, 5, 443, 443, 555, 555]) == 555
assert maximum([9]) == 9

assert get_min([-52, 56, 30, 29, -54, 0, -110]) == -110
assert get_min([42, 54, 65, 87, 0]) == 0
assert get_min([1, 2, 3, 4, 5, 10]) == 1
assert get_min([-1, -2, -3, -4, -5, -10]) == -10
assert get_min([9]) == 9

assert get_max([-52, 56, 30, 29, -54, 0, -110]) == 56
assert get_max([4, 6, 2, 1, 9, 63, -134, 566]) == 566
assert get_max([5]) == 5
assert get_max([534, 43, 2, 1, 3, 4, 5, 5, 443, 443, 555, 555]) == 555
assert get_max([9]) == 9
