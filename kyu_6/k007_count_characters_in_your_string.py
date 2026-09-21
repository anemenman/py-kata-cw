"""
Count characters in your string

The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result
should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.
"""
from collections import Counter


def count(text):
    return dict(Counter(text))


from collections import defaultdict


def count_v2(text):
    result = defaultdict(int)
    for char in text:
        result[char] += 1
    return dict(result)


assert count('aba') == {'a': 2, 'b': 1}
assert count('') == {}
assert count('aa') == {'a': 2}
assert count('aabb') == {'b': 2, 'a': 2}

assert count_v2('aba') == {'a': 2, 'b': 1}
assert count_v2('') == {}
assert count_v2('aa') == {'a': 2}
assert count_v2('aabb') == {'b': 2, 'a': 2}
