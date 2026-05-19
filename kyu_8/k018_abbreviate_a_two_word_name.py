"""
Abbreviate a Two Word Name

Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
The output should be two capital letters with a dot separating them.
It should look like this:

Sam Harris => S.H

patrick feeney => P.F
"""


def abbrev_name(name: str) -> str:
    first, last = name.split()
    return f"{first[0].upper()}.{last[0].upper()}"


# For any count of words
def abbrev_name2(name: str) -> str:
    return '.'.join(word[0].upper() for word in name.split())


assert abbrev_name("Sam Harris") == "S.H"
assert abbrev_name("patrick feenan") == "P.F"
assert abbrev_name("Evan C") == "E.C"
assert abbrev_name("P Favuzzi") == "P.F"
assert abbrev_name("David Mendieta") == "D.M"

assert abbrev_name2("Sam Harris") == "S.H"
assert abbrev_name2("patrick feenan") == "P.F"
assert abbrev_name2("Evan C") == "E.C"
assert abbrev_name2("P Favuzzi") == "P.F"
assert abbrev_name2("David Mendieta") == "D.M"
assert abbrev_name2("David Mendieta for any count of words") == "D.M.F.A.C.O.W"
