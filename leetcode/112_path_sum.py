"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: bool
        """
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == target

        if root.left and self.hasPathSum(root.left, target - root.val):
            return True

        if root.right and self.hasPathSum(root.right, target - root.val):
            return True

        return False
