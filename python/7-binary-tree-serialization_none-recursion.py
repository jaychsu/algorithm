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
        if not isinstance(root, TreeNode):
            return '{}'
        queue = [root]
        result = []
        for node in queue:
            if not isinstance(node, TreeNode):
                result.append('#')
                continue
            result.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)
        while result[-1] is '#':
            result.pop()
        return '{%s}' % ','.join(result)

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
        value = values.pop(0) if len(values) > 0 else '#'
        root = TreeNode(value) if value is not '#' else None
        queue = [root]
        index = -1
        while len(values) > 0:
            index += 1
            if queue[index] is None:
                continue
            value = values.pop(0)
            queue[index].left = TreeNode(value) if value is not '#' else None
            queue.append(queue[index].left)
            value = values.pop(0) if len(values) > 0 else '#'
            queue[index].right = TreeNode(value) if value is not '#' else None
            queue.append(queue[index].right)
        return root
