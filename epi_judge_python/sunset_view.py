from typing import Iterator, List

from test_framework import generic_test


def examine_buildings_with_sunset(sequence: List[int]) -> List[int]:
    stack: List[int] = []

    for i in range(len(sequence) - 1, -1, -1):
        if not len(stack) or sequence[i] > sequence[stack[-1]]:
            stack.append(i)

    return stack


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('sunset_view.py', 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
