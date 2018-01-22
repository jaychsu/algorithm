# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        if not root:
            return 0

        return (
            self.find_path(root, target) +
            self.pathSum(root.left, target) +
            self.pathSum(root.right, target)
        )

    def find_path(self, node, target):
        if not node:
            return 0

        return (
            int(node.val == target) +
            self.find_path(node.left, target - node.val) +
            self.find_path(node.right, target - node.val)
        )
