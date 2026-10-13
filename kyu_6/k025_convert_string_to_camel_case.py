"""
Convert string to camel case

Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word
within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also
often referred to as Pascal case). The next words should be always capitalized.

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"

"The_Stealth_Warrior" gets converted to "TheStealthWarrior"

"The_Stealth-Warrior" gets converted to "TheStealthWarrior"
"""


def to_camel_case(text):
    if not text:
        return text

    text = text.replace('_', '-')
    words = text.split('-')
    words = [w for w in words if w]

    if not words:
        return ''

    return words[0] + ''.join(w.capitalize() for w in words[1:])


assert to_camel_case("") == ""
assert to_camel_case("the_stealth_warrior") == "theStealthWarrior"
assert to_camel_case("The-Stealth-Warrior") == "TheStealthWarrior"
assert to_camel_case("A-B-C") == "ABC"
