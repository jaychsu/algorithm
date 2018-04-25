"""
Testing:

>>> class TreeNode:
...     def __init__(self, val):
...         self.val = val
...         self.left = self.right = None

>>> trees = []
>>> tree_infos = [
...     ((
...         (-3, None, None),
...     ), -3),
...     ((
...         (3, 4, 5),
...         (4, None, None),
...         (5, None, None),
...     ), 60),
...     ((
...         (3, 4, -5),
...         (4, None, None),
...         (-5, None, None),
...     ), 12),
...     ((
...         (3, 4, -5),
...         (4, -6, 7),
...         (-5, 2, -9),
...         (-6, None, None),
...         (7, None, None),
...         (2, None, None),
...         (-9, None, None),
...     ), 3780),
...     ((
...         (0, 4, -5),
...         (4, -6, 7),
...         (-5, 2, -9),
...         (-6, None, None),
...         (7, None, None),
...         (2, None, None),
...         (-9, None, None),
...     ), 90),
... ]

>>> for info, _ in tree_infos:
...     nodes = {node[0]: TreeNode(node[0]) for node in info}
...
...     for val, left, right in info:
...         if left:
...             nodes[val].left = nodes[left]
...         if right:
...             nodes[val].right = nodes[right]
...
...     trees.append(nodes[info[0][0]])

>>> gotcha = []
>>> s = Solution()
>>> for i in range(len(trees)):
...     res = s.maxPathProd(trees[i])
...     if res != tree_infos[i][1]: print(res, tree_infos[i])
...     gotcha.append(res == tree_infos[i][1])
>>> bool(gotcha) and all(gotcha)
True
"""


class Solution:
    def maxPathProd(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        ans, _, _ = self.divide_conquer(root)
        return ans

    def divide_conquer(self, node):
        if not node:
            return float('-inf'), 1, 1

        res_left, max_left, min_left = self.divide_conquer(node.left)
        res_right, max_right, min_right = self.divide_conquer(node.right)

        a = node.val * max(max_left, max_right)
        b = node.val * min(min_left, min_right)

        res = max(
            # ignoring current (0)
            res_left,
            res_right,
            # only current (1)
            node.val,
            # half path (2)
            a, b,
            # go through current (3)
            node.val * max_left * max_right,
            node.val * min_left * min_right,
        )

        return res, max(a, b), min(a, b)
