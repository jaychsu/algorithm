"""
Notice:
node A or node B may not exist in tree.


Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    def lowestCommonAncestor3(self, root, a, b):
        """
        :type root: TreeNode
        :type a: TreeNode
        :type b: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return

        lca, has_a, has_b = self.divide_conquer(root, a, b)

        return lca if has_a and has_b else None

    def divide_conquer(self, node, a, b):
        if not node:
            return None, False, False

        left, a_in_left, b_in_left = self.divide_conquer(node.left, a, b)
        right, a_in_right, b_in_right = self.divide_conquer(node.right, a, b)

        has_a = a_in_left or a_in_right or node is a
        has_b = b_in_left or b_in_right or node is b

        if node is a or node is b:
            return node, has_a, has_b
        if left and right:
            return node, has_a, has_b
        if left:
            return left, has_a, has_b
        if right:
            return right, has_a, has_b

        return None, has_a, has_b
