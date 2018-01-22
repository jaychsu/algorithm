# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def hasPathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: bool
        """
        return self.dfs(root, target)

    def dfs(self, node, remaining):
        if not node:
            return False

        remaining -= node.val
        if remaining == 0 and not node.left and not node.right:
            return True

        in_left = self.dfs(node.left, remaining)
        in_right = self.dfs(node.right, remaining)

        return in_left or in_right
