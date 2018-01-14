"""
Main Concept:
https://discuss.leetcode.com/topic/65792/recursive-easy-to-understand-java-solution


Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of the binary search tree.
    @param: target: Remove the node with given value.
    @return: The root of the binary search tree after removal.
    """
    def removeNode(self, root, target):
        if not root:
            return root

        if root.val == target:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            min_node = self.find_min(root.right)
            root.val = min_node.val
            root.right = self.removeNode(root.right, root.val)

            return root

        if target < root.val:
            root.left = self.removeNode(root.left, target)
        else:
            root.right = self.removeNode(root.right, target)

        return root

    def find_min(self, node):
        if not node:
            return node
        while node.left:
            node = node.left
        return node
