from test_framework import generic_test


def is_well_formed(s: str) -> bool:
    prev_chars = []
    close_dict = {
        ')': '(',
        '}': '{',
        ']': '[',
    }

    for char in s:
        if char not in close_dict:
            prev_chars.append(char)
        else:
            if len(prev_chars) and close_dict[char] == prev_chars[-1]:
                prev_chars.pop()
            else:
                return False

    return len(prev_chars) == 0


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('is_valid_parenthesization.py',
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
