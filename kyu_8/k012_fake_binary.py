"""
Fake Binary

Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the
resulting string.

Note: input will never be an empty string
"""


def fake_bin(s: str) -> str:
    return ''.join('0' if d < '5' else '1' for d in s)


assert fake_bin("45385593107843568") == "01011110001100111"
assert fake_bin("509321967506747") == "101000111101101"
assert fake_bin("366058562030849490134388085") == "011011110000101010000011011"
assert fake_bin("15889923") == "01111100"
assert fake_bin("800857237867") == "100111001111"
