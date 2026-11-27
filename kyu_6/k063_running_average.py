"""
Running Average

Python:
Create a function running_average() that returns a callable function object. Update the series with each given value
and calculate the current average.

r_avg = running_average()
r_avg(10) = 10.0
r_avg(11) = 10.5
r_avg(12) = 11
All input values are valid. Round to two decimal places.

This Kata is based on a example from Fluent Python book.

Javascript // Lua // C++:
Create a function runningAverage() that returns a callable function object. Update the series with each given value
and calculate the current average.

rAvg = runningAverage();
rAvg(10) = 10.0;
rAvg(11) = 10.5;
rAvg(12) = 11;
"""


def running_average():
    total = 0.0
    count = 0

    def _running_average(value):
        nonlocal total, count
        total += value
        count += 1
        return round(total / count, 2)

    return _running_average


r_avg = running_average()

assert r_avg(10) == 10
assert r_avg(11) == 10.5
assert r_avg(12) == 11
