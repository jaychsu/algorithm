# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        vals = []
        stack = []
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            vals.append(node.val)
            node = node.right

        ans = float('inf')

        for i in range(1, len(vals)):
            if vals[i] - vals[i - 1] < ans:
                ans = vals[i] - vals[i - 1]

        return ans
