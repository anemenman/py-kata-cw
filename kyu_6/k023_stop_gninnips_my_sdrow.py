"""
Stop gninnipS My sdroW!

Write a function that takes in a string of one or more words, and returns the same string, but with all words that have
five or more letters reversed (just like the name of this kata). Strings passed in will consist of only letters and
spaces. Words will be separated by exactly one space. There will be no leading or trailing spaces.

Examples:

"Hey fellow warriors"  --> "Hey wollef sroirraw"
"This is a test        --> "This is a test"
"This is another test" --> "This is rehtona test"
"""


def spin_words(sentence):
    return ' '.join(word[::-1] if len(word) >= 5 else word for word in sentence.split())


assert spin_words("Welcome") == "emocleW"
assert spin_words("to") == "to"
assert spin_words("CodeWars") == "sraWedoC"
assert spin_words("Hey fellow warriors") == "Hey wollef sroirraw"
assert spin_words("This sentence is a sentence") == "This ecnetnes is a ecnetnes"
