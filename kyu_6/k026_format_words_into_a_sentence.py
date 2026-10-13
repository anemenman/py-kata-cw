"""
Format words into a sentence

Complete the method so that it formats the words into a single comma separated value. The last word should be
separated by the word 'and' instead of a comma. The method takes in an array of strings and returns a single
formatted string.

Note:

Empty string values should be ignored.
Empty arrays or null/nil/None values being passed into the method should result in an empty string being returned.
Example: (Input --> output)

['ninja', 'samurai', 'ronin'] --> "ninja, samurai and ronin"
['ninja', '', 'ronin'] --> "ninja and ronin"
[] -->""
"""


def format_words(words):
    if not words:
        return ''

    filtered = [w for w in words if w]

    if not filtered:
        return ''

    if len(filtered) == 1:
        return filtered[0]

    if len(filtered) == 2:
        return f'{filtered[0]} and {filtered[1]}'

    return ', '.join(filtered[:-1]) + ' and ' + filtered[-1]


assert format_words(['one', 'two', 'three', 'four']) == 'one, two, three and four'
assert format_words(['one']) == 'one'
assert format_words(['one', '', 'three']) == 'one and three'
assert format_words(['', '', 'three']) == 'three'
assert format_words(['one', 'two', '']) == 'one and two'
assert format_words([]) == ''
assert format_words(None) == ''
assert format_words(['']) == ''
