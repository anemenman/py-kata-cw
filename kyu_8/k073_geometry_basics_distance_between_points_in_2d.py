"""
Geometry Basics: Distance between points in 2D

This series of katas will introduce you to basics of doing geometry with computers.
Point objects have attributes x and y.
Write a function calculating distance between Point a and Point b.
Input coordinates fit in range
−50⩽x,y⩽50
−50⩽x,y⩽50. Tests compare expected result and actual answer with tolerance of 1e-6.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance_between_points(a, b):
    return ((a.x - b.x) ** 2 + (a.y - b.y) ** 2) ** 0.5


assert round(distance_between_points(Point(3, 3), Point(3, 3)), 6) == 0
assert round(distance_between_points(Point(1, 6), Point(4, 2)), 6) == 5
assert round(distance_between_points(Point(-10.2, 12.5), Point(0.3, 14.7)), 6) == 10.728001
