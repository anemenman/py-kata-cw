"""
Volume of a Cuboid

Bob needs a fast way to calculate the volume of a rectangular cuboid with three values: the length, width and height of
the cuboid.

Write a function to help Bob with this calculation.
"""


def get_volume_of_cuboid(length: float, width: float, height: float) -> float:
    return length * width * height


assert get_volume_of_cuboid(1, 2, 2) == 4
assert get_volume_of_cuboid(6.3, 2, 5) == 63
