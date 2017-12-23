"""
Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
"""


class Solution:
    """
    @param: root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        max_size, _, _ = self.divide_conquer(root)
        return max_size

    def divide_conquer(self, node):
        if not node:
            return 0, 0, 0

        max_size = 1
        max_up_size = max_down_size = 0
        for branch in ('left', 'right'):
            child = getattr(node, branch)
            if not child:
                continue

            _max, _up, _down = self.divide_conquer(child)
            if node.val == child.val + 1 and _up + 1 > max_up_size:
                max_up_size = _up + 1
            if node.val == child.val - 1 and _down + 1 > max_down_size:
                max_down_size = _down + 1
            if _max > max_size:
                max_size = _max

        if max_up_size + max_down_size + 1 > max_size:
            max_size = max_up_size + max_down_size + 1

        return max_size, max_up_size, max_down_size
