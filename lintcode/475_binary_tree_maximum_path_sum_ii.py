"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree.
    @return: An integer
    """
    def maxPathSum2(self, root):
        return self.divide_conquer(root)

    def divide_conquer(self, node):
        if not node:
            return 0

        left_sum = self.divide_conquer(node.left)
        right_sum = self.divide_conquer(node.right)

        # '0' is included, since no need to end at leaf
        return node.val + max(0, left_sum, right_sum)
