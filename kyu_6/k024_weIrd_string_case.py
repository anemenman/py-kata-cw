"""
WeIrD StRiNg CaSe

Write a function that accepts a string, and returns the same string with all even indexed characters in each word upper
cased, and all odd indexed characters in each word lower cased. The indexing just explained is zero based, so the
zeroth index is even, therefore that character should be upper cased. Indexing resets for each word. In other words,
the first letter of every word is index 0 (even), so it must always be uppercase, etc.

The passed in string will only consist of alphabetical characters and spaces(' '). Spaces will only be present if there
are multiple words. Words will be separated by a single space(' ').

Examples:
"String" => "StRiNg"
"Weird string case" => "WeIrD StRiNg CaSe"
"""


def to_weird_case(string):
    words = string.split(' ')
    result = []

    for word in words:
        weird_word = ''
        for i, char in enumerate(word):
            if i % 2 == 0:
                weird_word += char.upper()
            else:
                weird_word += char.lower()
        result.append(weird_word)

    return ' '.join(result)


assert to_weird_case('This') == 'ThIs'
assert to_weird_case('is') == 'Is'
assert to_weird_case('THIs iS a TEST') == 'ThIs Is A TeSt'
