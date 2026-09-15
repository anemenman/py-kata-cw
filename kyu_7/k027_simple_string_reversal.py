"""
Simple string reversal

In this Kata, we are going to reverse a string while maintaining the spaces (if any) in their original place.

For example:

"our code" => "edo cruo"
-- Normal reversal without spaces is "edocruo".
-- However, there is a space at index 3, so the string becomes "edo cruo"

"your code rocks" => "skco redo cruoy".
"codewars" => "srawedoc"
More examples in the test cases. All input will be lower case letters and in some cases spaces.

Good luck!
"""


def solve(s: str) -> str:
    reversed_chars = [c for c in s if c != ' '][::-1]
    char_iter = iter(reversed_chars)

    return ''.join(next(char_iter) if c != ' ' else ' ' for c in s)


assert solve('codewars') == 'srawedoc'
assert solve('your code') == 'edoc ruoy'
assert solve('your code rocks') == 'skco redo cruoy'
assert solve('i love codewars') == 's rawe docevoli'
