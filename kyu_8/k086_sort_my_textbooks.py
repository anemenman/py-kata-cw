"""
Sort My Textbooks

HELP! Jason can't find his textbook! It is two days before the test date, and Jason's textbooks are all out of order!
Help him sort a list (ArrayList in java) full of textbooks by subject, so he can study before the test.

The sorting should NOT be case sensitive
"""


def sorter(textbooks):
    textbooks.sort(key=lambda book: book.casefold())
    return textbooks


def sorter2(textbooks):
    # return sorted(textbooks, key=str.casefold)
    return sorted(textbooks, key=lambda book: book.casefold())


assert sorter(['Algebra', 'History', 'Geometry', 'English']) == ['Algebra', 'English', 'Geometry',
                                                                 'History']
assert sorter(['Algebra', 'history', 'Geometry', 'english']) == ['Algebra', 'english', 'Geometry',
                                                                 'history']
assert sorter(['Alg#bra', '$istory', 'Geom^try', '**english']) == ['$istory', '**english', 'Alg#bra',
                                                                   'Geom^try']

assert sorter2(['Algebra', 'History', 'Geometry', 'English']) == ['Algebra', 'English', 'Geometry',
                                                                  'History']
assert sorter2(['Algebra', 'history', 'Geometry', 'english']) == ['Algebra', 'english', 'Geometry',
                                                                  'history']
assert sorter2(['Alg#bra', '$istory', 'Geom^try', '**english']) == ['$istory', '**english', 'Alg#bra',
                                                                    'Geom^try']
