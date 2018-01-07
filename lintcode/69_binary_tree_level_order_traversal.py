"""
Main Concept:
1. Use `_queue` to collect node in current level
2. Use `level_values` to collect the val of node in current level
3. After traverse the current level,
   append `level_values` to answer
   and reset `queue` as `_queue`

Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param: root: A Tree
    @return: Level order a list of lists of integer
    """
    def levelOrder(self, root):
        ans = []
        if not root:
            return ans

        queue = [root]

        while queue:
            _queue = []
            path = []

            for node in queue:
                if node.left:
                    _queue.append(node.left)
                if node.right:
                    _queue.append(node.right)

                path.append(node.val)

            ans.append(path)
            queue = _queue

        return ans
