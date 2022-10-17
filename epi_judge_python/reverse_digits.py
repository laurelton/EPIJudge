from test_framework import generic_test


def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    x = abs(x)
    x_rev = 0

    while x != 0:
        x_rev = (x_rev * 10) + x % 10
        x = x // 10

    return x_rev * sign


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('reverse_digits.py',
                                       'reverse_digits.tsv', reverse))
