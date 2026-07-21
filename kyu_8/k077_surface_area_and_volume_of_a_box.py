"""
Surface Area and Volume of a Box

Write a function that returns the total surface area and volume of a box.
The given input will be three positive non-zero integers: width, height, and depth.
The output will be language dependant, so please check sample tests for the corresponding data type,
(list, tuple, struct, query, etcetera).
"""


def get_size(w, h, d):
    surface_area = 2 * (w * h + w * d + h * d)
    volume = w * h * d
    return [surface_area, volume]


assert get_size(4, 2, 6) == [88, 48]
assert get_size(1, 1, 1) == [6, 1]
assert get_size(1, 2, 1) == [10, 2]
assert get_size(1, 2, 2) == [16, 4]
assert get_size(10, 10, 10) == [600, 1000]
