"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    EMPTY = '#'

    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        TEMPLATE = '{{{}}}'  # {{, }} is to escape brackets
        if not root:
            return TEMPLATE.format('')

        vals = []
        queue = [root]

        for node in queue:
            if not node:
                vals.append(self.EMPTY)
                continue

            vals.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        while vals[-1] == self.EMPTY:
            vals.pop()

        return TEMPLATE.format(','.join(vals))

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if (not data or
            data[0] != '{' or
            data[-1] != '}' or
            len(data) < 3 or
            data[1] == '#'
        ):
            return

        vals = data[1:-1].split(',')
        n = len(vals)
        i = 0

        root = TreeNode(int(vals[i]))
        queue = [root]

        for node in queue:
            for branch in ('left', 'right'):
                i += 1

                if i >= n:
                    break
                if vals[i] == self.EMPTY:
                    continue

                setattr(node, branch, TreeNode(int(vals[i])))
                queue.append(getattr(node, branch))

        return root
