"""
Find the unique number

There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""


def find_uniq(arr):
    # We use the observation that among the first three elements, at least two will be "common" (identical). This is
    # sufficient to determine the common value and then find the different element in a single pass.
    if arr[0] == arr[1]:
        common = arr[0]
    elif arr[0] == arr[2]:
        common = arr[0]
    else:
        common = arr[1]

    for x in arr:
        if x != common:
            return x

    return None


assert find_uniq([1, 1, 1, 2, 1, 1]) == 2
assert find_uniq([0, 0, 0.55, 0, 0]) == 0.55
assert find_uniq([3, 10, 3, 3, 3]) == 10
