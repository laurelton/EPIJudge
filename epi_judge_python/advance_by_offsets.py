from typing import List

from test_framework import generic_test


def can_reach_end(A: List[int]) -> bool:
    max_index = 0
    for i, val in enumerate(A):
        if max_index >= i:
            max_index = max(val + i, max_index)

    return max_index >= len(A) - 1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
