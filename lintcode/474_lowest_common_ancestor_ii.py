"""
The node has an extra attribute parent which point to the father of itself.
The root's parent is null.


Definition of ParentTreeNode:
class ParentTreeNode:
    def __init__(self, val):
        self.val = val
        self.parent, self.left, self.right = None, None, None
"""


class Solution:
    def lowestCommonAncestorII(self, root, a, b):
        """
        :type root: ParentTreeNode
        :type a: ParentTreeNode
        :type b: ParentTreeNode
        :rtype: ParentTreeNode
        """
        if not root:
            return root

        nodes = set()

        while a:
            nodes.add(a)
            a = a.parent

        while b:
            if b in nodes:
                return b
            b = b.parent

        return root
