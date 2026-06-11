"""
Is this my tail?

Some new animals have arrived at the zoo. The zoo keeper is concerned that perhaps the animals do not have the right
tails. To help her, you must correct the broken function to make sure that the second argument (tail), is the same as
the last letter of the first argument (body) - otherwise the tail wouldn't fit!
If the tail is right return true, else return false.

The arguments will always be non empty strings, and normal letters.
"""


def correct_tail(body: str, tail: str) -> bool:
    return body[-1] == tail


assert correct_tail("Fox", "x") == True
assert correct_tail("Rhino", "o") == True
assert correct_tail("Meerkat", "t") == True
assert correct_tail("Emu", "t") == False
assert correct_tail("Cat", "t") == True
