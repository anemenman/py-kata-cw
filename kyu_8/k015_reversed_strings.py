"""
Reversed Strings

Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
"""


def solution(s: str) -> str:
    return s[::-1]  # slicing


def solution2(s: str) -> str:
    return ''.join(reversed(s))


assert solution('world') == 'dlrow'
assert solution('hello') == 'olleh'
assert solution('') == ''
assert solution('h') == 'h'

assert solution2('world') == 'dlrow'
assert solution2('hello') == 'olleh'
assert solution2('') == ''
assert solution2('h') == 'h'
