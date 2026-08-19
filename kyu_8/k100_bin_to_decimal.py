"""
Bin to Decimal

Complete the function which converts a binary number (given as a string) to a decimal number.
"""


def bin_to_decimal(binary):
    return int(binary, 2)


assert bin_to_decimal('0') == 0
assert bin_to_decimal('1') == 1
assert bin_to_decimal('10') == 2
assert bin_to_decimal('11') == 3
assert bin_to_decimal('101010') == 42
assert bin_to_decimal('1001001') == 73
