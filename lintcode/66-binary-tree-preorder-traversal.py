"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Preorder in ArrayList which contains node values.
    """
    def preorderTraversal(self, root):
        ans = []
        if not root:
            return ans
        self._traversal(root, ans)
        return ans

    def _traversal(self, node, res):
        if not node:
            return

        res.append(node.val)
        self._traversal(node.left, res)
        self._traversal(node.right, res)
