"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        return self.divide_conquer(root, 0, 0)

    def divide_conquer(self, node, parent_val, max_size):
        if not node:
            return 0

        size = 1
        if parent_val + 1 == node.val:
            size += max_size

        left_size = self.divide_conquer(node.left, node.val, size)
        right_size = self.divide_conquer(node.right, node.val, size)

        return max(size, left_size, right_size)
