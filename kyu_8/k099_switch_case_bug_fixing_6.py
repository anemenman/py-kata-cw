"""
Switch/Case - Bug Fixing #6

Oh no! Timmy's evalObject function doesn't work. He uses Switch/Cases to evaluate the given properties of an object,
can you fix timmy's function?

def eval_object(v):
    match "operation":
        case "+":
            return v["a"] + v["b"]
        case "-":
            return v["a"] - v["b"]
        case "/":
            return v["a"] / v["b"]
        case "*":
            return v["a"] * v["b"]
        case "%":
            return v["a"] % v["b"]
        case "**":
            return v["a"] ** v["b"]
        case _:
            return 1
"""


def eval_object(v):
    a, b = v["a"], v["b"]
    match v["operation"]:
        case "+":
            return a + b
        case "-":
            return a - b
        case "*":
            return a * b
        case "/":
            return a / b
        case "%":
            return a % b
        case "**":
            return a ** b
    return None


assert eval_object({'a': 1, 'b': 1, 'operation': '+'}) == 2
assert eval_object({'a': 1, 'b': 1, 'operation': '-'}) == 0
assert eval_object({'a': 1, 'b': 1, 'operation': '/'}) == 1
assert eval_object({'a': 1, 'b': 1, 'operation': '*'}) == 1
assert eval_object({'a': 1, 'b': 1, 'operation': '%'}) == 0
assert eval_object({'a': 1, 'b': 1, 'operation': '**'}) == 1
