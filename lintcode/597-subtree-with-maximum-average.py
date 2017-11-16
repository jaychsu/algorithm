"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""

"""
Test Case:

{1,-5,11,1,2,4,-2}
: subtree_avg = subtree_sum / subtree_size -> subtree_avg = subtree_sum * 1.0 / subtree_size

{-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16}
: max_avg = 0 -> max_avg = float('-inf')
"""

class Solution:
    max_avg = float('-inf')
    max_node = None

    """
    @param: root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        self._traversal(root)
        return self.max_node

    def _traversal(self, node):
        if not node:
            return 0, 0

        left_sum, left_size = self._traversal(node.left)
        right_sum, right_size = self._traversal(node.right)

        subtree_sum = left_sum + right_sum + node.val
        subtree_size = left_size + right_size + 1
        subtree_avg = subtree_sum * 1.0 / subtree_size

        if subtree_avg > self.max_avg:
            self.max_avg = subtree_avg
            self.max_node = node

        return subtree_sum, subtree_size
