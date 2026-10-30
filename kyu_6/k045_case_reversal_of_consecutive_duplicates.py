"""
Case Reversal of Consecutive Duplicates

The aim of this Kata is to write a function which will reverse the case of all consecutive duplicate letters in a
string. That is, any letters that occur one after the other and are identical.

If the duplicate letters are lowercase then they must be set to uppercase, and if they are uppercase then they need
to be changed to lowercase.

Examples:

"puzzles" --> "puZZles"
"massive" --> "maSSive"
"LITTLE"  --> "LIttLE"
"shhh"    --> "sHHH"
Arguments passed will include only alphabetical letters A–Z or a–z.
"""

from itertools import groupby


def reverse(text):
    result = []
    for key, group in groupby(text):
        chars = list(group)
        if len(chars) >= 2:
            result.extend(c.swapcase() for c in chars)
        else:
            result.extend(chars)
    return ''.join(result)


assert reverse('hello world') == 'heLLo world'
assert reverse('HELLO WORLD') == 'HEllO WORLD'
assert reverse('HeLlo World') == 'HeLlo World'
assert reverse('WWW') == 'www'
