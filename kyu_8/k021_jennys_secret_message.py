"""
Jenny's secret message

Jenny has written a function that returns a greeting for a user. However, she's in love with Johnny, and would like to
greet him slightly different. She added a special case to her function, but she made a mistake.

Can you help her?
"""


def greet(name):
    return "Hello, my love!" if name == "Johnny" else f"Hello, {name}!"


assert greet("James") == "Hello, James!"
assert greet("Jane") == "Hello, Jane!"
assert greet("Jim") == "Hello, Jim!"
assert greet("Johnny") == "Hello, my love!"
