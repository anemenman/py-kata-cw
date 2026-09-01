"""
I'm everywhere!

Overview
Many people know that Apple uses the letter "i" in almost all of its devices to emphasize its personality.

And so John, a programmer at Apple, was given the task of making a program that would add that letter to every word.
Let's help him do it, too.

Task:
Your task is to make a function that takes the value of word and returns it with an "i" at the beginning of the word.
For example we get the word "Phone", so we must return "iPhone". But we have a few rules:

The word should not begin with the letter "I", for example Inspire.
The number of vowels should not be greater than or equal to the number of consonants, for example East or Peace. ("y"
is considered a consonant)
The first letter should not be lowercase, for example road.
If the word does not meet the rules, we return "Invalid word".
"""


def i(word):
    if not word or word[0].islower() or word[0] == 'I':
        return 'Invalid word'

    vowels = set('aeiouAEIOU')
    vowel_count = sum(1 for c in word if c in vowels)
    consonant_count = sum(1 for c in word if c.isalpha() and c not in vowels)

    if vowel_count >= consonant_count:
        return 'Invalid word'

    return 'i' + word


assert i('Phone') == 'iPhone'
assert i('World') == 'iWorld'
assert i('Human') == 'iHuman'
assert i('Programmer') == 'iProgrammer'

assert i('') == 'Invalid word'
assert i('Inspire') == 'Invalid word'
assert i('East') == 'Invalid word'
assert i('Peace') == 'Invalid word'
assert i('road') == 'Invalid word'
