"""
Longest Palindrome

Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.

Example:
"a" -> 1
"aab" -> 2
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
"""


# Manacher's Algorithm (O(n))
# If the string is very long (millions of characters), you can use Manacher's Algorithm, which finds all palindromes in
# linear time, reusing the results of previous extensions:
def longest_palindrome(s):
    if not s:
        return 0

    t = '^#' + '#'.join(s) + '#$'
    p = [0] * len(t)
    center = right = 0
    max_len = 0

    for i in range(1, len(t) - 1):
        mirror = 2 * center - i

        if i < right:
            p[i] = min(right - i, p[mirror])

        while t[i + p[i] + 1] == t[i - p[i] - 1]:
            p[i] += 1

        if i + p[i] > right:
            center, right = i, i + p[i]

        max_len = max(max_len, p[i])

    return max_len


assert longest_palindrome('a') == 1
assert longest_palindrome('aa') == 2
assert longest_palindrome('baa') == 2
assert longest_palindrome('aab') == 2
assert longest_palindrome('abcdefghba') == 1
assert longest_palindrome('baablkj12345432133d') == 9
