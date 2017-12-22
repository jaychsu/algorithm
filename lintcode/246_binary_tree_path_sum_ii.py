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
        self.dfs(root, 1, target, ans, [])
        return ans

    def dfs(self, node, depth, target, ans, path):
        if not node:
            return

        path += [node.val]

        remaining = target
        for i in range(depth - 1, -1, -1):
            remaining -= path[i]
            if remaining == 0:
                ans.append(path[i:])

        depth += 1
        self.dfs(node.left, depth, target, ans, path[:])
        self.dfs(node.right, depth, target, ans, path[:])
