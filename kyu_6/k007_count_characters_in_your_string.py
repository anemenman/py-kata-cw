"""
Count characters in your string

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result
should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""
from collections import Counter


def count(text):
    return dict(Counter(text))


assert count('aba') == {'a': 2, 'b': 1}
assert count('') == {}
assert count('aa') == {'a': 2}
assert count('aabb') == {'b': 2, 'a': 2}
