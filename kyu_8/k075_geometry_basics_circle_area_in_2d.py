"""
Geometry Basics: Circle Area in 2D

This series of katas will introduce you to basics of doing geometry with computers.

Write the function circleArea/CircleArea which takes in a Circle object and calculates the area of that circle.
The Circle class can be seen below:

class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius
And the Point class can be seen below:

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
"""
import math


class Circle:
    def __init__(self, center, radius):
        self.center = center
        self.radius = radius


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def circle_area(circle):
    return math.pi * (circle.radius ** 2)


assert circle_area(Circle(Point(10, 10), 30)) == 2827.4333882308138
assert circle_area(Circle(Point(25, -70), 30)) == 2827.4333882308138
assert circle_area(Circle(Point(-15, 5), 0)) == 0.0
assert circle_area(Circle(Point(-15, 5), 12.5)) == 490.8738521234052
