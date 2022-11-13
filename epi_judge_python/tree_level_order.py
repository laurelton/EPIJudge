from typing import List
from collections import deque

from binary_tree_node import BinaryTreeNode
from test_framework import generic_test


def binary_tree_depth_order(tree: BinaryTreeNode) -> List[List[int]]:
    result = []
    if not tree:
        return result

    curr_level = [tree]
    while curr_level:
        level_data = []
        for node in curr_level:
            level_data.append(node.data)

        result.append(level_data)
        child_nodes = []
        for node in curr_level:
            if node.left:
                child_nodes.append(node.left)
            if node.right:
                child_nodes.append(node.right)

        curr_level = child_nodes

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('tree_level_order.py',
                                       'tree_level_order.tsv',
                                       binary_tree_depth_order))
