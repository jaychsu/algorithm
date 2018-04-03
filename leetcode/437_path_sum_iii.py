"""
Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    find path count
    """
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        if not root:
            return 0

        return sum((
            self.count_valid_path(root, target),
            self.pathSum(root.left, target),
            self.pathSum(root.right, target),
        ))

    def count_valid_path(self, node, remaining):
        if not node:
            return 0

        return sum((
            int(node.val == remaining),
            self.count_valid_path(node.left, remaining - node.val),
            self.count_valid_path(node.right, remaining - node.val),
        ))


class Solution:
    """
    print path
    """
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: list[list[int]]
        """
        ans = []

        if not root:
            return ans

        self.dfs(root, target, ans, [])

        return ans

    def dfs(self, node, target, ans, path):
        if not node:
            return

        path.append(node.val)

        remaining = target
        for i in range(len(path) - 1, -1, -1):
            remaining -= path[i]

            if remaining == 0:
                ans.append(path[i:])

        self.dfs(node.left, target, ans, path)
        self.dfs(node.right, target, ans, path)
        path.pop()
