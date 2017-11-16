"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    res = []

    """
    @param: root: the root of the binary tree
    @return: all root-to-leaf paths
    """
    def binaryTreePaths(self, root):
        if not root:
            return []
        self._traversal(root, [])
        return self.res

    def _traversal(self, node, parents):
        parents.append(str(node.val))

        if not node.left and not node.right:
            self.res.append('->'.join(parents))
            # remove the leaf node in parent
            parents.pop()
            return

        if node.left:
            self._traversal(node.left, parents)
        if node.right:
            self._traversal(node.right, parents)
        # after visited both child node, remove current node
        # and will continue to visit the siblings node
        parents.pop()
