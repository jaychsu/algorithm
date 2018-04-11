"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    def maxPathSum2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        left = self.maxPathSum2(root.left)
        right = self.maxPathSum2(root.right)

        return root.val + max(0, left, right)
