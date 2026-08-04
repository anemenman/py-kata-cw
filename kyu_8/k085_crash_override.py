"""
Crash Override

Every budding hacker needs an alias! The Phantom Phreak, Acid Burn, Zero Cool and Crash Override are some notable
examples from the film Hackers.

Your task is to create a function that, given a proper first and last name, will return the correct alias.

Notes:
Two objects that return a one word name in response to the first letter of the first name and one for the first letter
of the surname are already given. See the examples below for further details.

If the first character of either of the names given to the function is not a letter from A - Z, you should return "Your
name must start with a letter from A - Z."

Sometimes people might forget to capitalize the first letter of their name so your function should accommodate for
these grammatical errors.

Examples
# These two dictionaries are preloaded, you need to use them in your code
FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', ...}
SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst' ...}

alias_gen('Larry', 'Brentwood') == 'Logic Bomb'
alias_gen('123abc', 'Petrovic') == 'Your name must start with a letter from A - Z.'
Happy hacking!
"""
FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache', 'D': 'Data', 'H': 'Half-life', 'F': 'Function', 'M': 'Malware',
              'W': 'WiFi'}
SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst', 'K': 'Killer', 'M': 'Mike', 'P': 'Payload', 'T': 'T-Rex',
           'W': 'Worm'}


def alias_gen(first_name, last_name):
    error_message = 'Your name must start with a letter from A - Z.'

    try:
        first_key = first_name[0].upper()
        last_key = last_name[0].upper()
    except (TypeError, IndexError):
        return error_message

    if first_key in FIRST_NAME and last_key in SURNAME:
        return f'{FIRST_NAME[first_key]} {SURNAME[last_key]}'

    return error_message


assert alias_gen('Mike', 'Millington') == 'Malware Mike'
assert alias_gen('Fahima', 'Tash') == 'Function T-Rex'
assert alias_gen('Daisy', 'Petrovic') == 'Data Payload'
assert alias_gen('Barny', 'White') == 'Beta Worm'
assert alias_gen('Hank', 'Kutz') == 'Half-life Killer'
assert alias_gen('123abc', 'Pinkman') == 'Your name must start with a letter from A - Z.'
assert alias_gen('walter', 'white') == 'WiFi Worm'
