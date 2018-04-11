"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

        return self.divide_conquer(root.left, root.right)

    def divide_conquer(self, left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        if not self.divide_conquer(left.left, right.right):
            return False
        if not self.divide_conquer(left.right, right.left):
            return False
        return True
