"""
Counting sheep...

Consider an array/list of sheep where some sheep may be missing from their place. We need a function that counts the
number of sheep present in the array (true means present).

For example,

[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True, True]
The correct answer would be 18.

Hint: Don't forget to check for bad values like null/undefined
"""


def count_sheeps(sheep):
    return sheep.count(True)


assert count_sheeps([True, True, True, False,
                     True, True, True, True,
                     True, False, True, False,
                     True, False, False, True,
                     True, True, True, True,
                     False, False, True, True, True]) == 18

assert count_sheeps([None, True, True, None,
                     True, True, True, True,
                     True, False, True, False,
                     True, False, False, True]) == 10
