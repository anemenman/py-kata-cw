"""
Custom Array Filters

Dave has a lot of data he is required to apply filters to, which are simple enough, but he wants a shorter way of
doing so.

He wants the following functions to work as expected:

even # list([1,2,3,4,5]).even() should return [2,4]
odd # list([1,2,3,4,5]).odd() should return [1,3,5]
under # list([1,2,3,4,5]).under(4) should return [1,2,3]
over # list([1,2,3,4,5]).over(4) should return [5]
in_range # list([1,2,3,4,5]).in_range(1, 3) should return [1,2,3]
They should also work when used together, for example:

list(list([1,2,3,4,5,6,7,8,9,10]).even()).under(5) # should return [2,4]
And finally the filters should only accept integer values from an array, for example:

list(["a", 1, "b", 300, "x", "q", 63, 122, 181, "z", 0.83, 0.11]).even() // should return [300, 122]
Note: List with non-numbers will be tested as well.
"""


class list(list):
    def _get_ints(self):
        return [x for x in self if type(x) is int]

    def even(self):
        return list([x for x in self._get_ints() if x % 2 == 0])

    def odd(self):
        return list([x for x in self._get_ints() if x % 2 != 0])

    def under(self, n):
        return list([x for x in self._get_ints() if x < n])

    def over(self, n):
        return list([x for x in self._get_ints() if x > n])

    def in_range(self, min_val, max_val):
        return list([x for x in self._get_ints() if min_val <= x <= max_val])


assert list([1, 2, 3, 4, 5]).even() == [2, 4]
assert list([1, 2, 3, 4, 5]).odd() == [1, 3, 5]
assert list([1, 2, 3, 4, 5]).under(4) == [1, 2, 3]
assert list([1, 2, 3, 4, 5]).over(4) == [5]
assert list([1, 2, 3, 4, 5]).over(10) == []
assert list([1, 2, 3, 4, 5]).in_range(1, 3) == [1, 2, 3]
assert list(["a", "b", "c"]).under(10) == []
assert list(["a", "b", "c"]).over(10) == []
assert list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).over(10) == []
assert list(list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]).even()).under(5) == [2, 4]
assert list(["a", 1, "b", 300, "x", "q", 63, 122, 181, "z", 0.83, 0.11]).even() == [300, 122]
