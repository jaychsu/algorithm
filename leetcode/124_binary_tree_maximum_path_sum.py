# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        self.ans = float('-inf')
        self.divide_conquer(root)
        return self.ans

    def divide_conquer(self, node):
        if not node:
            return 0

        left_sum = max(0, self.divide_conquer(node.left))
        right_sum = max(0, self.divide_conquer(node.right))

        self.ans = max(self.ans, node.val + left_sum + right_sum)

        return node.val + max(left_sum, right_sum)
