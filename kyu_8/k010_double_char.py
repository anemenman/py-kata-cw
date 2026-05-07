"""
Double Char

Given a string, you have to return a string in which each character (case-sensitive) is repeated once.

Examples (Input -> Output):
* "String"      -> "SSttrriinngg"
* "Hello World" -> "HHeelllloo  WWoorrlldd"
* "1234!_ "     -> "11223344!!__  "
"""


def double_char(s: str) -> str:
    return "".join(c * 2 for c in s)


assert double_char("String") == "SSttrriinngg"
assert double_char("Hello World") == "HHeelllloo  WWoorrlldd"
assert double_char("1234!_ ") == "11223344!!__  "

# lambda:
# double_char2 = lambda s: "".join(c * 2 for c in s)
# print(double_char2("String"))
# print(double_char2("Hello World"))
