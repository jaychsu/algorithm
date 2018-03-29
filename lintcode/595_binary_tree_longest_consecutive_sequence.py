"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
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
        seg_size = 0

        for branch in ('left', 'right'):
            child = getattr(node, branch)
            if not child:
                continue

            _size, _seg_size = self.divide_conquer(child)

            if child.val - 1 == node.val and _seg_size + 1 > seg_size:
                seg_size = _seg_size + 1

            if _size > size:
                size = _size

        if seg_size + 1 > size:
            size = seg_size + 1

        return size, seg_size


class Solution:
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return self.divide_conquer(root, 0, 0)

    def divide_conquer(self, node, parent_val, max_size):
        if not node:
            return 0

        size = 1

        if parent_val + 1 == node.val:
            size += max_size

        left = self.divide_conquer(node.left, node.val, size)
        right = self.divide_conquer(node.right, node.val, size)

        return max(size, left, right)
