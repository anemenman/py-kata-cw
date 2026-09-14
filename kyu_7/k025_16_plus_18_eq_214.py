"""
16+18=214

For this kata you will have to forget how to add two numbers.

It can be best explained using the following meme:

Dayane Rivas adding up a sum while competing in the Guatemalan television show "Combate" in May 2016

In simple terms, our method does not like the principle of carrying over numbers and just writes down every number it
calculates :-)

You may assume both integers are positive integers.
"""


def add(num1, num2):
    s1 = str(num1)
    s2 = str(num2)

    max_len = max(len(s1), len(s2))
    s1 = s1.zfill(max_len)
    s2 = s2.zfill(max_len)

    result = ''.join(str(int(d1) + int(d2)) for d1, d2 in zip(s1, s2))

    return int(result)


assert add(2, 11) == 13
assert add(0, 1) == 1
assert add(0, 0) == 0

assert add(16, 18) == 214
assert add(26, 39) == 515
assert add(122, 81) == 1103
