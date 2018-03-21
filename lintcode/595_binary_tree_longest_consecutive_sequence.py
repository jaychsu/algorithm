"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
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
