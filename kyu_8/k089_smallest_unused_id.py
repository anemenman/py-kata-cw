"""
Smallest unused ID

Hey awesome programmer!

You've got much data to manage and of course you use zero-based and non-negative ID's to make each data item unique!

Therefore you need a method, which returns the smallest unused ID for your next new data item...

Note: The given array of used IDs may be unsorted. For test reasons there may be duplicate IDs, but you don't have to
find or remove them!

Go on and code some pure awesomeness!
"""


def next_id(arr):
    used = set(arr)
    candidate = 0

    while candidate in used:
        candidate += 1

    return candidate


assert next_id([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 11
assert next_id([5, 4, 3, 2, 1]) == 0
assert next_id([0, 1, 2, 3, 5]) == 4
assert next_id([0, 0, 0, 0, 0, 0]) == 1
