"""
The path could be start and end at any node in the tree


Definition for a multi tree node.
class MultiTreeNode(object):
    def __init__(self, x):
        self.val = x
        children = [] # children is a list of MultiTreeNode
"""


class Solution:
    """
    Bottom Up
    """
    def longestConsecutive3(self, root):
        """
        :type root: MultiTreeNode
        :rtype: int
        """
        if not root:
            return 0

        return self.divide_conquer(root)[0]

    def divide_conquer(self, node):
        if not node:
            return 0, 0, 0

        size = 1
        up = down = 0

        for child in node.children:
            if not child:
                continue

            _size, _up, _down = self.divide_conquer(child)

            if child.val + 1 == node.val and _up + 1 > up:
                up = _up + 1

            if child.val - 1 == node.val and _down + 1 > down:
                down = _down + 1

            if _size > size:
                size = _size

        if up + down + 1 > size:
            size = up + down + 1

        return size, up, down
