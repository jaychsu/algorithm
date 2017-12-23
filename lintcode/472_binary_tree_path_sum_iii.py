"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @param: target: An integer
    @return: all valid paths
    """
    def binaryTreePathSum3(self, root, target):
        """
        1. using `dfs` to visit every node in that tree
        2. once enter a node, start to find the path based on it
           to parent, left child, and right child.
        """
        ans = []
        self.dfs(root, target, ans)
        return ans

    def dfs(self, node, target, ans):
        if not node:
            return

        self.find_path(node, node, target, ans, [])

        self.dfs(node.left, target, ans)
        self.dfs(node.right, target, ans)

    def find_path(self, node, start, remaining, ans, path):
        path.append(node.val)

        remaining -= node.val
        if remaining == 0:
            ans.append(path[:])

        if node.parent and node.parent is not start:
            self.find_path(node.parent, node, remaining, ans, path)
        if node.left and node.left is not start:
            self.find_path(node.left, node, remaining, ans, path)
        if node.right and node.right is not start:
            self.find_path(node.right, node, remaining, ans, path)

        path.pop()
