"""
Notice:
Assume two nodes are exist in tree.


Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    def lowestCommonAncestor(self, root, a, b):
        """
        :type root: TreeNode
        :type a: TreeNode
        :type b: TreeNode
        :rtype: TreeNode
        """
        if not root or root is a or root is b:
            return root

        left = self.lowestCommonAncestor(root.left, a, b)
        right = self.lowestCommonAncestor(root.right, a, b)

        if left and right:
            return root
        if left:
            return left
        if right:
            return right
