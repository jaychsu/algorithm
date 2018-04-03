"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        if not root:
            return ans

        self.dfs(root, target, ans, [])

        return ans

    def dfs(self, node, remaining, ans, path):
        if not node:
            return

        path.append(node.val)

        if not node.left and not node.right and remaining == node.val:
            ans.append(path[:])
        else:
            self.dfs(node.left, remaining - node.val, ans, path)
            self.dfs(node.right, remaining - node.val, ans, path)

        path.pop()
