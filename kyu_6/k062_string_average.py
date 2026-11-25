"""
String average

You are given a string of numbers between 0-9. Find the average of these numbers and return it as a floored whole
number (ie: no decimal places) written out as a string. Eg:

"zero nine five two" -> "four"

If the string is empty or includes a number greater than 9, return "n/a"
"""

word_to_num = {
    'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4,
    'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}


def average_string(s):
    if not s or s.strip() == '':
        return 'n/a'
    num_to_word = {v: k for k, v in word_to_num.items()}

    words = s.split()
    nums = []

    for w in words:
        w_lower = w.lower()
        if w_lower in word_to_num:
            nums.append(word_to_num[w_lower])
        else:
            return 'n/a'

    if not nums:
        return 'n/a'

    avg = sum(nums) / len(nums)
    floored = int(avg)

    if floored in num_to_word:
        return num_to_word[floored]
    else:
        return 'n/a'


assert average_string('zero nine five two') == 'four'
assert average_string('four six two three') == 'three'
assert average_string('one two three four five') == 'three'
assert average_string('five four') == 'four'
assert average_string('zero zero zero zero zero') == 'zero'
assert average_string('one one eight one') == 'two'
assert average_string('one') == 'one'
assert average_string('') == 'n/a'
assert average_string('ten') == 'n/a'
assert average_string('pippi') == 'n/a'
