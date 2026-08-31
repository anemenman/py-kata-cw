"""
Exes and Ohs

Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case
insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false
"""


def xo(s: str) -> bool:
    s = s.lower()
    return s.count('x') == s.count('o')


assert xo('ooxx') == True
assert xo('xooxx') == False
assert xo('ooxXm') == True
assert xo('zpzpzpp') == True
assert xo('zzoo') == False
assert xo('oxOx') == True
assert xo('') == True
