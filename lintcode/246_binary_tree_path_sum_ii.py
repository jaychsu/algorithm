"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum2(self, root, target):
        ans = []
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
