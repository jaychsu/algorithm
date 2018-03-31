"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if not root:
            return float('-inf')

        if root.left and target < root.val:
            left = self.closestValue(root.left, target)

            if abs(left - target) < abs(root.val - target):
                return left

        if root.right and target > root.val:
            right = self.closestValue(root.right, target)

            if abs(right - target) < abs(root.val - target):
                return right

        return root.val
