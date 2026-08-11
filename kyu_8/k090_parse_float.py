"""
Parse float

Write function parse_float which takes a string/list and returns a number or 'none' if conversion is not possible.
"""


def parse_float(x):
    try:
        # If a string is passed, ''.join(x) returns the same text.
        # If list strings are passed, it will concatenate them into a single string.
        return float(''.join(x))
    except (ValueError, TypeError):
        return None


assert parse_float('1.0') == 1.0
assert parse_float('a') is None
assert parse_float('234.0234') == 234.0234
