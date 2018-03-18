"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: list[str]
        """
        ans = []
        if not root:
            return ans

        self.dfs(root, ans, [])

        return ans

    def dfs(self, node, ans, path):
        path.append(str(node.val))

        if not node.left and not node.right:
            ans.append('->'.join(path))
            path.pop()
            return

        if node.left:
            self.dfs(node.left, ans, path)

        if node.right:
            self.dfs(node.right, ans, path)

        path.pop()
