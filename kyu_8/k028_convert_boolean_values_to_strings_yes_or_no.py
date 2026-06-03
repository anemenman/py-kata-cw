"""
Convert boolean values to strings 'Yes' or 'No'.

Complete the method that takes a boolean value and return a "Yes" string for true, or a "No" string for false.
"""


def bool_to_word(boolean):
    return 'Yes' if boolean else 'No'


assert bool_to_word(True) == 'Yes'
assert bool_to_word(False) == 'No'
