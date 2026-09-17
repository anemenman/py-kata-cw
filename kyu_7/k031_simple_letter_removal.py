"""
Simple letter removal

In this Kata, you will be given a lower case string and your task will be to remove k characters from that string using
the following rule:

- first remove all letter 'a', followed by letter 'b', then 'c', etc...
- remove the leftmost character first.
For example:
solve('abracadabra', 1) = 'bracadabra' # remove the leftmost 'a'.
solve('abracadabra', 2) = 'brcadabra'  # remove 2 'a' from the left.
solve('abracadabra', 6) = 'rcdbr'      # remove 5 'a', remove 1 'b'
solve('abracadabra', 8) = 'rdr'
solve('abracadabra',50) = ''
More examples in the test cases. Good luck!
"""


def solve(s, k):
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if k == 0:
            break
        count = s.count(c)
        if count <= k:
            s = s.replace(c, '')
            k -= count
        else:
            result = []
            removed = 0
            for char in s:
                if char == c and removed < k:
                    removed += 1
                else:
                    result.append(char)
            s = ''.join(result)
            k = 0
    return s


assert solve('abracadabra', 1) == 'bracadabra'
assert solve('abracadabra', 2) == 'brcadabra'
assert solve('abracadabra', 6) == 'rcdbr'
assert solve('abracadabra', 8) == 'rdr'
assert solve('abracadabra', 50) == ''
assert solve('hxehmvkybeklnj', 5) == 'xmvkyklnj'
assert solve('cccaabababaccbc', 3) == 'cccbbabaccbc'
assert solve('cccaabababaccbc', 9) == 'cccccc'
assert solve('u', 1) == ''
assert solve('back', 3) == 'k'
