"""
Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    def lowestCommonAncestorII(self, root, A, B):
        """
        :type root: ParentTreeNode
        :type A: int
        :type B: int
        :rtype: int
        """
        nodes = {}

        while A:
            nodes[A] = True
            A = A.parent

        while B:
            if B in nodes:
                return B
            B = B.parent

        return root
