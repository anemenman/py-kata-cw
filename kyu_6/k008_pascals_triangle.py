"""
Pascal's Triangle

In mathematics, Pascal's triangle is a triangular array of the binomial coefficients expressed with formula, where n
denotes a row of the triangle, and k is a position of a term in the row.
You can read Wikipedia article on Pascal's Triangle for more information.

Task
Write a function that, given a depth n, returns n top rows of Pascal's Triangle flattened into a one-dimensional
list/array.

Example:
n = 1: [1]
n = 2: [1,  1, 1]
n = 4: [1,  1, 1,  1, 2, 1,  1, 3, 3, 1]
"""


def pascals_triangle(n: int) -> list[int]:
    result = []
    prev_row = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = prev_row[j - 1] + prev_row[j]
        result.extend(row)
        prev_row = row
    return result


assert pascals_triangle(1) == [1]
assert pascals_triangle(2) == [1, 1, 1]
assert pascals_triangle(3) == [1, 1, 1, 1, 2, 1]
