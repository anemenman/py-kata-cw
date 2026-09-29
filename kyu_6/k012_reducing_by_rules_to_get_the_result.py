"""
Reducing by rules to get the result

Reducing by rules to get the result
Your task is to reduce a list of numbers to one number.
For this you get a list of rules, how you have to reduce the numbers.
You have to use these rules consecutively. So when you get to the end of the list of rules, you start again at the
beginning.

An example is clearer than more words...

numbers: [ 2.0, 2.0, 3.0, 4.0 ]
rules: [ (a,b) => a + b, (a,b) => a - b ]
result: 5.0

You get a list of four numbers.
There are two rules. First rule says: Sum the two numbers a and b. Second rule says: Subtract b from a.

The steps in progressing:
1. Rule 1: First number + second number -> 2.0 + 2.0 = 4.0
2. Rule 2: result from step before - third number -> 4.0 - 3.0 = 1.0
3. Rule 1: result from step before + forth number -> 1.0 + 4.0 = 5.0
Both lists/arrays are never null and will always contain valid elements.
The list of numbers will always contain more than 1 numbers.
In the list of numbers will only be values greater than 0.
Every rule takes always two input parameter.


Have fun coding it and please don't forget to vote and rank this kata! :-)

I have also created other katas. Take a look if you enjoyed this kata!
"""


def reduce_by_rules(numbers, rules):
    result = numbers[0]
    rule_idx = 0

    for num in numbers[1:]:
        result = rules[rule_idx](result, num)
        rule_idx = (rule_idx + 1) % len(rules)

    return result


rules = [lambda a, b: a + b, lambda a, b: a - b]
assert reduce_by_rules([2.0, 2.0, 3.0, 4.0], rules) == 5.0

rules = [lambda a, b: a + b]
assert reduce_by_rules([2.0, 2.0, 2.0], rules) == 6.0
assert reduce_by_rules([2.0, 2.0, 2.0, 2.0], rules) == 8.0
assert reduce_by_rules([2.0, 2.0, 2.0, 2.0, 2.0], rules) == 10.0
assert reduce_by_rules([2.0, 2.0, 2.0, 2.0, 2.0, 2.0], rules) == 12.0

rules = [lambda a, b: a + b, lambda a, b: a - b, lambda a, b: a * b]
assert reduce_by_rules([2.0, 2.0, 2.0], rules) == 2.0
assert reduce_by_rules([2.0, 2.0, 2.0, 2.0], rules) == 4.0
assert reduce_by_rules([2.0, 2.0, 2.0, 2.0, 2.0], rules) == 6.0
assert reduce_by_rules([2.0, 2.0, 2.0, 2.0, 2.0, 2.0], rules) == 4.0

rules = [min, max]
assert reduce_by_rules([1.3, 2.0, 3.3], rules) == 3.3
assert reduce_by_rules([4.1, 2.2, 2.1, 2.5], rules) == 2.2
assert reduce_by_rules([8.0, 8.1, 4.1, 12.0, 2.0], rules) == 8.0
assert reduce_by_rules([2.9, 2.8, 2.7, 2.6, 2.5, 2.4], rules) == 2.4
