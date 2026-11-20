"""
Hamming Distance

The Hamming Distance is a measure of similarity between two strings of equal length. Complete the function so that it
returns the number of positions where the input strings do not match.

Examples:
a = "I like turtles"
b = "I like turkeys"
Result: 3

a = "Hello World"
b = "Hello World"
Result: 0

a = "espresso"
b = "Expresso"
Result: 2
You can assume that the two inputs are ASCII strings of equal length.
"""


def hamming(a, b):
    return sum(1 for char_a, char_b in zip(a, b) if char_a != char_b)


assert hamming('hello world', 'hello tokyo') == 4
assert hamming('a man a plan a canal', 'a man a plan sobanal') == 3
assert hamming('hamming and cheese', 'Hamming and Cheese') == 2
assert hamming('espresso', 'Expresso') == 2
assert hamming('old father, old artificer', 'of my soul the uncreated ') == 24
