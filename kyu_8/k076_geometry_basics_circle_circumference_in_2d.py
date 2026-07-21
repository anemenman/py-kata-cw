"""
Geometry Basics: Circle Circumference in 2D

This series of katas will introduce you to basics of doing geometry with computers.
Point objects have x, y attributes. Circle objects have center which is a Point, and radius, which is a number.
Write a function calculating circumference of a Circle.

Tests round answers to 6 decimal places.
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


def circle_circumference(circle):
    return 2 * math.pi * circle.radius


assert round(circle_circumference(Circle(Point(10, 10), 30)), 6) == 188.495559
assert round(circle_circumference(Circle(Point(25, -70), 30)), 6) == 188.495559
assert round(circle_circumference(Circle(Point(-15, 5), 0)), 6) == 0
assert round(circle_circumference(Circle(Point(-15, 5), 12.5)), 6) == 78.539816
