"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        ans = 0
        if not root:
            return ans

        queue = [root]
        while queue:
            _queue = []
            ans += 1

            for node in queue:
                if not node.left and not node.right:
                    return ans
                if node.left:
                    _queue.append(node.left)
                if node.right:
                    _queue.append(node.right)

            queue = _queue

        return ans


class Solution:
    """
    @param: root: The root of binary tree
    @return: An integer
    """
    def minDepth(self, root):
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)

        if left == 0:
            return right + 1
        if right == 0:
            return left + 1

        return min(left, right) + 1
