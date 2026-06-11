"""
Enumerable Magic - Does My List Include This?


Create a method that accepts a list and an item, and returns true if the item belongs to the list, otherwise false.
"""


def include(arr, item):
    return item in arr


lst = [0, 1, 2, 3, 5, 8, 13, 2, 2, 2, 11]
assert include(lst, 100) == False
assert include(lst, 2) == True
assert include(lst, 11) == True
assert include(lst, "2") == False
assert include(lst, 0) == True
assert include([], 0) == False
