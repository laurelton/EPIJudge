from test_framework import generic_test
from math import floor, log10

def is_palindrome_number(x: int) -> bool:
    if x < 0:
        return False

    if x < 10: 
        return True

    num_digits = floor(log10(x)) + 1
    msd_mask = 10 ** (num_digits - 1)

    for _ in range(num_digits // 2):
        first = x // msd_mask
        last = x % 10
        if first != last:
            return False

        # Remove first digit
        x = x % msd_mask
        # Remove last digit
        x = x // 10
        # Adjust Most Significant Digit mask
        msd_mask = msd_mask // 100

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_number_palindromic.py',
                                       'is_number_palindromic.tsv',
                                       is_palindrome_number))
