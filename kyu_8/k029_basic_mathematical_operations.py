"""
Basic Mathematical Operations

Your task is to create a function that does four basic mathematical operations.

The function should take three arguments - operation(string/char), value1(number), value2(number).
The function should return result of numbers after applying the chosen operation.

Examples(Operator, value1, value2) --> output
('+', 4, 7) --> 11
('-', 15, 18) --> -3
('*', 5, 5) --> 25
('/', 49, 7) --> 7
"""
import operator


def basic_op(operation, value1, value2):
    if operation == '+':
        return value1 + value2
    elif operation == '-':
        return value1 - value2
    elif operation == '*':
        return value1 * value2
    elif operation == '/':
        return value1 / value2
    else:
        raise ValueError('Not supported operation')


def basic_op_v2(operation, value1, value2):
    actions = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    return actions[operation](value1, value2)


assert basic_op('+', 4, 7) == 11
assert basic_op('-', 15, 18) == -3
assert basic_op('*', 5, 5) == 25
assert basic_op('/', 49, 7) == 7
