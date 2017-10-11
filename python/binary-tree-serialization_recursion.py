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
        if any([
            not isinstance(root, TreeNode),
            root is None,
        ]):
            return '{}'
        result = self._serialize(root)
        return '{%s}' % ','.join([str(val) if val is not None else '#' for val in result])

    def _serialize(self, node, result = []):
        if node is None:
            result.append(None)
        else:
            result.append(node.val)
            self._serialize(node.left, result)
            self._serialize(node.right, result)
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
        if any([
            not isinstance(data, str),
            data is '{}',
            data[0] is not '{' and data[-1] is not '}'
        ]):
            return
        return self._deserialize(data[1:-1].split(','))

    def _deserialize(self, reference):
        val = reference.pop(0) if len(reference) > 0 else '#'
        if val is '#':
            return
        node = TreeNode(val)
        node.left = self._deserialize(reference)
        node.right = self._deserialize(reference)
        return node
