"""
Is your period late?

In this kata, we will make a function to test whether a period is late.

Our function will take three parameters:

last - The Date object with the date of the last period

today - The Date object with the date of the check

cycleLength - Integer representing the length of the cycle in days

Return true if the number of days passed from last to today is greater than cycleLength. Otherwise, return false.
"""
from datetime import date


def period_is_late(last, today, cycle_length):
    days_passed = (today - last).days
    return days_passed > cycle_length


assert period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35) == False
assert period_is_late(date(2016, 6, 13), date(2016, 7, 16), 28) == True
assert period_is_late(date(2016, 6, 13), date(2016, 7, 16), 35) == False
assert period_is_late(date(2016, 6, 13), date(2016, 6, 29), 28) == False
assert period_is_late(date(2016, 7, 12), date(2016, 8, 9), 28) == False
