"""
Calculate String Rotation

Write a function that receives two strings and returns n, where n is equal to the number of characters we should shift
the first string forward to match the second. The check should be case sensitive.

For instance, take the strings "fatigue" and "tiguefa". In this case, the first string has been rotated 5 characters
forward to produce the second string, so 5 would be returned.

If the second string isn't a valid rotation of the first string, the method returns -1.
Examples:
"coffee", "eecoff" => 2
"eecoff", "coffee" => 4
"moose", "Moose" => -1
"isn't", "'tisn" => 2
"Esham", "Esham" => 0
"dog", "god" => -1
"""


def shifted_diff(s1, s2):
    if len(s1) != len(s2):
        return -1
    if len(s1) == 0:
        return 0

    doubled = s1 + s1
    idx = doubled.find(s2)

    if idx == -1:
        return -1

    return (len(s1) - idx) % len(s1)


assert shifted_diff("eecoff", "coffee") == 4
assert shifted_diff("Moose", "moose") == -1
assert shifted_diff("isn't", "'tisn") == 2
assert shifted_diff("Esham", "Esham") == 0
assert shifted_diff(" ", " ") == 0
assert shifted_diff("hoop", "pooh") == -1
assert shifted_diff("  ", " ") == -1
