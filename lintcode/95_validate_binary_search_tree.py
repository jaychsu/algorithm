"""
Main Concept:
since the fact,
if we said a tree is NOT a binary search tree,
and then the values we got by inorder traversal
is must be a non-descending sequence, that is, A[i+1] >= A[i].


Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        node = root

        val = None

        while stack or node:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            if val is not None and val >= node.val:
                return False
            else:
                val = node.val

            node = node.right

        return True


class Solution:
    is_valid = True
    last_val = None

    """
    @param: root: The root of binary tree.
    @return: True if the binary tree is BST, or false
    """
    def isValidBST(self, root):
        self._divide_conquer(root)
        return self.is_valid

    def _divide_conquer(self, node):
        if not node:
            return

        self._divide_conquer(node.left)

        # since the demands, we can only accept the ascending sequence
        if self.last_val and node.val <= self.last_val:
            self.is_valid = False
            return
        self.last_val = node.val

        self._divide_conquer(node.right)
