"""
Simple Encryption #1 - Alternating Split

Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed
characters of S with all the even-indexed characters of S, this process should be repeated N times.

Examples:

encrypt("012345", 1)  =>  "135024"
encrypt("012345", 2)  =>  "135024"  ->  "304152"
encrypt("012345", 3)  =>  "135024"  ->  "304152"  ->  "012345"

encrypt("01234", 1)  =>  "13024"
encrypt("01234", 2)  =>  "13024"  ->  "32104"
encrypt("01234", 3)  =>  "13024"  ->  "32104"  ->  "20314"
Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.
"""


def encrypt(text, n):
    if not text or n <= 0:
        return text

    for _ in range(n):
        text = text[1::2] + text[0::2]

    return text


def decrypt(text, n):
    if not text or n <= 0:
        return text

    for _ in range(n):
        length = len(text)
        k = length // 2

        result = [''] * length
        result[0::2] = text[k:]
        result[1::2] = text[:k]

        text = ''.join(result)

    return text


assert encrypt("This is a test!", 0) == "This is a test!"
assert encrypt("This is a test!", 1) == "hsi  etTi sats!"
assert encrypt("This is a test!", 2) == "s eT ashi tist!"
assert encrypt("This is a test!", 3) == " Tah itse sits!"
assert encrypt("This is a test!", 4) == "This is a test!"
assert encrypt("This is a test!", -1) == "This is a test!"
assert encrypt("This kata is very interesting!", 1) == "hskt svr neetn!Ti aai eyitrsig"

assert decrypt("This is a test!", 0) == "This is a test!"
assert decrypt("hsi  etTi sats!", 1) == "This is a test!"
assert decrypt("s eT ashi tist!", 2) == "This is a test!"
assert decrypt(" Tah itse sits!", 3) == "This is a test!"
assert decrypt("This is a test!", 4) == "This is a test!"
assert decrypt("This is a test!", -1) == "This is a test!"
assert decrypt("hskt svr neetn!Ti aai eyitrsig", 1) == "This kata is very interesting!"

assert encrypt("", 0) == ""
assert decrypt("", 0) == ""
assert encrypt(None, 0) is None
assert decrypt(None, 0) is None
