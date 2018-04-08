"""
The longest consecutive path need to be from parent to child (cannot be the reverse).


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
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return self.divide_conquer(root)[0]

    def divide_conquer(self, node):
        if not node:
            return 0, 0

        size = 1
        down = 0

        for branch in ('left', 'right'):
            child = getattr(node, branch)

            if not child:
                continue

            _size, _down = self.divide_conquer(child)

            if child.val - 1 == node.val and _down + 1 > down:
                down = _down + 1

            if _size > size:
                size = _size

        if down + 1 > size:
            size = down + 1

        return size, down


class Solution:
    """
    Top Down
    """
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return self.divide_conquer(root, 0, 0)

    def divide_conquer(self, node, parent_val, _size):
        if not node:
            return 0

        size = 1

        if parent_val + 1 == node.val:
            size += _size

        left = self.divide_conquer(node.left, node.val, size)
        right = self.divide_conquer(node.right, node.val, size)

        return max(size, left, right)
