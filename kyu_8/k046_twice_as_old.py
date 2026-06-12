"""
Twice as old

Your function takes two arguments:

current father's age (years)
current age of his son (years)
Calculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old).
The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.
"""


def twice_as_old(father_age, son_age):
    return abs(father_age - 2 * son_age)


assert twice_as_old(36, 7) == 22
assert twice_as_old(55, 30) == 5
assert twice_as_old(42, 21) == 0
assert twice_as_old(22, 1) == 20
