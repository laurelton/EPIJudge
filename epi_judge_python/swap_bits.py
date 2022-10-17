from test_framework import generic_test


def swap_bits(x, i, j):
    # Shift x right by 'i' bits then 'and' 1 to test if the bit is set
    i_is_set = (x >> i) & 1 
    j_is_set = (x >> j) & 1
    # If the bits are the same we don't need to swap them
    if i_is_set != j_is_set:
        # Create a bit mask where only 'i' and 'j' are set
        # (1 << i) will set the ith bit
        # 'or' creates a mask with both bits set
        bit_mask = (1 << i) | (1 << j)
        # 'xor' flips bits
        x = x ^ bit_mask

    return x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('swap_bits.py', 'swap_bits.tsv',
                                       swap_bits))
