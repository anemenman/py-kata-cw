"""
Points of Reflection

"Point reflection" or "point symmetry" is a basic concept in geometry where a given point, P, at a given position
relative to a mid-point, Q has a corresponding point, P1, which is the same distance from Q but in the opposite
direction.

Task
Given two points P and Q, output the symmetric point of point P about Q. Each argument is a two-element array of
integers representing the point's X and Y coordinates. Output should be in the same format, giving the X and Y
coordinates of point P1. You do not have to validate the input.
"""


# The formula that requires a segment looks like this:
# Qx = (Px + P1x) / 2
# Qy = (Py + P1y) / 2
# Let us express from here the coordinates of the desired point P1:
# P1x = 2 * Qx - Px
# P1y = 2 * Qy - Py
def symmetric_point(p, q):
    x1 = 2 * q[0] - p[0]
    y1 = 2 * q[1] - p[1]

    return [x1, y1]


assert symmetric_point([0, 0], [1, 1]) == [2, 2]
assert symmetric_point([2, 6], [-2, -6]) == [-6, -18]
assert symmetric_point([10, -10], [-10, 10]) == [-30, 30]
assert symmetric_point([1, -35], [-12, 1]) == [-25, 37]
assert symmetric_point([1000, 15], [-7, -214]) == [-1014, -443]
assert symmetric_point([0, 0], [0, 0]) == [0, 0]
