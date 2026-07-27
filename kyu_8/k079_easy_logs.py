"""
easy logs

Given a logarithm base X and two values A and B, return a sum of logratihms with the base X: logxA + logxB
"""
import math


def logs(x, a, b):
    return math.log(a * b, x)


assert logs(5, 2, 3) == 1.1132827525593785
assert logs(1000, 2, 3) == 0.25938375012788123
assert logs(2, 1, 2) == 1
assert logs(0.00001, 0.002, 0.01) == 0.9397940008672038
assert logs(0.1, 0.002, 0.01) == 4.69897000433602
