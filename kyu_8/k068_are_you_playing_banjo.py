"""
Are You Playing Banjo?

Create a function which answers the question "Are you playing banjo?".
If your name starts with the letter "R" or lower case "r", you are playing banjo!

The function takes a name as its only argument, and returns one of the following strings:

name + " plays banjo"
name + " does not play banjo"
Names given are always valid strings.
"""


def are_you_playing_banjo(name):
    if name[0].lower() == 'r':
        return f"{name} plays banjo"
    return f"{name} does not play banjo"


assert are_you_playing_banjo("martin") == "martin does not play banjo"
assert are_you_playing_banjo("Rikke") == "Rikke plays banjo"
assert are_you_playing_banjo("bravo") == "bravo does not play banjo"
assert are_you_playing_banjo("rolf") == "rolf plays banjo"
