"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: T1: The roots of binary tree T1.
    @param: T2: The roots of binary tree T2.
    @return: True if T2 is a subtree of T1, or false.
    """
    def isSubtree(self, T1, T2):
        if not T2:
            return True
        if not T1:
            return False

        if self.isEqual(T1, T2):
            return True

        return (self.isSubtree(T1.left,  T2) or
                self.isSubtree(T1.right, T2))

    def isEqual(self, T1, T2):
        if not T1 or not T2:
            return T1 is T2

        if T1.val != T2.val:
            return False

        return (self.isEqual(T1.left,  T2.left) and
                self.isEqual(T1.right, T2.right))
