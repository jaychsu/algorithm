"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    NULL_NODE = '#'

    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        if not isinstance(root, TreeNode):
            return '{}'

        queue = [root]
        values = []

        for node in queue:
            if not node:
                values.append(self.NULL_NODE)
                continue

            queue.append(node.left)
            queue.append(node.right)
            values.append(str(node.val))

        while values[-1] == self.NULL_NODE:
            values.pop()

        return '{%s}' % ','.join(values)

    """
    @param data: A string serialized by your serialize method.
    This method will be invoked second, the argument data is what exactly
    you serialized at method "serialize", that means the data is not given by
    system, it's given by your own serialize method. So the format of data is
    designed by yourself, and deserialize it here as you serialize it in
    "serialize" method.
    """
    def deserialize(self, data):
        if not isinstance(data, str) \
                or data[0] != '{' \
                or data[-1] != '}':
            return

        values = data[1:-1].split(',')
        if not values:
            return
        value = values.pop(0)
        if value == self.NULL_NODE:
            return

        root = TreeNode(value)
        queue = [root]

        for node in queue:
            if not values:
                break
            value = values.pop(0)
            if value != self.NULL_NODE:
                node.left = TreeNode(value)
                queue.append(node.left)

            if not values:
                break
            value = values.pop(0)
            if value != self.NULL_NODE:
                node.right = TreeNode(value)
                queue.append(node.right)

        return root
