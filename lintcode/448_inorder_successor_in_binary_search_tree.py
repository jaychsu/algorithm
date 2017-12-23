"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: The root of the BST.
    @param: p: You need find the successor node of p.
    @return: Successor of p.
    """
    def inorderSuccessor(self, root, p):
        if not root or not p:
            return

        stack = []
        node = root
        got_target = False

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            if got_target:
                return node
            if node.val == p.val:
                got_target = True

            node = node.right
