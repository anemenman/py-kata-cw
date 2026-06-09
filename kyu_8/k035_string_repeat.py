"""
String repeat

Write a function that accepts a non-negative integer n and a string s as parameters, and returns a string of s repeated
exactly n times.

Examples (input -> output)
6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
"""


def repeat_str(repeat, string):
    return string * repeat


assert repeat_str(4, 'a') == 'aaaa'
assert repeat_str(3, 'hello ') == 'hello hello hello '
assert repeat_str(2, 'abc') == 'abcabc'
assert repeat_str(0, '') == ''
assert repeat_str(0, 'I') == ''
assert repeat_str(5, '') == ''
assert repeat_str(6, 'I') == 'IIIIII'
assert repeat_str(5, 'Hello') == 'HelloHelloHelloHelloHello'
