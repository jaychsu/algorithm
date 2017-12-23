"""
Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""


class Solution:
    # @param {MultiTreeNode} root the root of k-ary tree
    # @return {int} the length of the longest consecutive sequence path
    def longestConsecutive3(self, root):
        max_size, _, _ = self.divide_conquer(root)
        return max_size

    def divide_conquer(self, node):
        if not node:
            return 0, 0, 0

        max_size = 1
        max_up_size = max_down_size = 0
        for child in node.children:
            _max, _up, _down = self.divide_conquer(child)
            # `+1` in `_up` and `_down` means that `child`
            if node.val == child.val + 1 and _up + 1 > max_up_size:
                max_up_size = _up + 1
            if node.val == child.val - 1 and _down + 1 > max_down_size:
                max_down_size = _down + 1
            if _max > max_size:
                max_size = _max

        # `+1` means `node` self
        if max_up_size + max_down_size + 1 > max_size:
            max_size = max_up_size + max_down_size + 1

        return max_size, max_up_size, max_down_size
