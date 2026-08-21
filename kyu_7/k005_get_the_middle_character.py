"""
Get the Middle Character

You are going to be given a non-empty string. Your job is to return the middle character(s) of the string.

If the string's length is odd, return the middle character.
If the string's length is even, return the middle 2 characters.
Examples:
"test" --> "es"
"testing" --> "t"
"middle" --> "dd"
"A" --> "A"
"""


# If the length is odd (e.g., 7): (7-1)//2 = 3, and 7//2 + 1 = 4. The slice s[3:4] will return exactly one character
# (with index 3).
# If the length is even (e.g., 4): (4-1)//2 = 1, and 4//2 + 1 = 3. The slice s[1:3] will return exactly two characters
# (with indices 1 and 2).
def get_middle(s):
    return s[(len(s) - 1) // 2: len(s) // 2 + 1]


assert get_middle('test') == 'es'
assert get_middle('testing') == 't'
assert get_middle('middle') == 'dd'
