"""
Reversed Strings

Complete the solution so that it reverses the string passed into it.

'world'  =>  'dlrow'
'word'   =>  'drow'
"""


def solution(s: str) -> str:
    return s[::-1]  # slicing


assert solution('world') == 'dlrow'
assert solution('hello') == 'olleh'
assert solution('') == ''
assert solution('h') == 'h'
