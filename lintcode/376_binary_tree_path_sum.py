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
    def binaryTreePathSum(self, root, target):
        ans = []
        self.dfs(root, target, ans, [])
        return ans

    def dfs(self, node, remaining, ans, path):
        if not node:
            return

        path.append(node.val)

        remaining -= node.val
        if remaining == 0 and not node.left and not node.right:
            ans.append(path[:])

        self.dfs(node.left, remaining, ans, path)
        self.dfs(node.right, remaining, ans, path)

        path.pop()
