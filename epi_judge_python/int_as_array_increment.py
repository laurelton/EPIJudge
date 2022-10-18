from typing import List

from test_framework import generic_test


def plus_one(A: List[int]) -> List[int]:
    i = len(A) - 1
    carry = 1
    while carry == 1 and i >= 0:
        val = carry + A[i]
        carry, val = val // 10, val % 10
        A[i] = val

        i -= 1

    if carry == 1:
        A = [carry] + A

    return A


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('int_as_array_increment.py',
                                       'int_as_array_increment.tsv', plus_one))
