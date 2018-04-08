"""
The path could be start and end at any node in the tree


If use top down in this case, still need return the result from bottom
=> just use bottom up


Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    Bottom Up
    """
    def longestConsecutive2(self, root):
        """
        :type root: TreeNode
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

        for branch in ('left', 'right'):
            child = getattr(node, branch)

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
