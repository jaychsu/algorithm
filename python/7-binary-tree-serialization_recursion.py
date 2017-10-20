"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: An object of TreeNode, denote the root of the binary tree.
    This method will be invoked first, you should design your own algorithm
    to serialize a binary tree which denote by a root node to a string which
    can be easily deserialized by your own "deserialize" method later.
    """
    def serialize(self, root):
        if isinstance(root, TreeNode):
            return '{%s}' % ','.join(self._serialize(root, []))
        return '{}'

    def _serialize(self, node, result):
        if isinstance(node, TreeNode):
            result.append(str(node.val))
            self._serialize(node.left, result)
            self._serialize(node.right, result)
        else:
            result.append('#')
        return result

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
            or data is '{}' \
            or data[0] is not '{' \
            or data[-1] is not '}':
            return
        values = data[1:-1].split(',')
        root = TreeNode(values.pop(0))
        self._deserialize(root, values)
        return root

    def _deserialize(self, node, values):
        if len(values) < 1:
            return
        value = values.pop(0)
        if value is not '#':
            node.left = TreeNode(value)
            self._deserialize(node.left, values)
        if len(values) < 1:
            return
        value = values.pop(0)
        if value is not '#':
            node.right = TreeNode(value)
            self._deserialize(node.right, values)
