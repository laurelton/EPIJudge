from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    l = len(A) - 1
    for r, val in reversed(list(enumerate(A))):
        if r + val >= l:
            l = r

    return l == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
