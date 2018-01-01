"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: A list of lists of integer include the zigzag level order traversal of its nodes' values.
    """
    def zigzagLevelOrder(self, root):
        ans = []
        if not root:
            return ans

        queue = [root]
        while queue:
            _queue = []
            ans.append([])

            for node in queue:
                if node.left:
                    _queue.append(node.left)
                if node.right:
                    _queue.append(node.right)

                ans[-1].append(node.val)

            if len(ans) % 2 == 0:
                ans[-1].reverse()

            queue = _queue

        return ans
