"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        ans, _ = self.divide_conquer(root)
        return ans

    def divide_conquer(self, node):
        if not node:
            return float('-inf'), 0

        max_left, left = self.divide_conquer(node.left)
        max_right, right = self.divide_conquer(node.right)

        # 0 means discard the negative path
        res = max(max_left, max_right, node.val + left + right)
        path = max(node.val + left, node.val + right, 0)

        return res, path


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.ans = float('-inf')
        self.divide_conquer(root)
        return self.ans

    def divide_conquer(self, node):
        if not node:
            return 0

        left = max(0, self.divide_conquer(node.left))
        right = max(0, self.divide_conquer(node.right))

        if node.val + left + right > self.ans:
            self.ans = node.val + left + right

        return node.val + max(left, right)
