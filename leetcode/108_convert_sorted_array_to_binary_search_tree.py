# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def sortedArrayToBST(self, A):
        """
        :type A: List[int]
        :rtype: TreeNode
        """
        if not A:
            return

        i = len(A) // 2
        node = TreeNode(A[i])
        node.left = self.sortedArrayToBST(A[:i])
        node.right = self.sortedArrayToBST(A[i + 1:])
        return node
