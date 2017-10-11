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
        queue = [root]
        for node in queue:
            if node is not None:
                queue.append(node.left)
                queue.append(node.right)
        while queue[-1] is None:
            queue.pop()
        return '{%s}' % ','.join([str(node.val) if node is not None else '#' for node in queue])

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
        reference = data[1:-1].split(',')
        val = reference.pop(0)
        root = TreeNode(val) if val is not '#' else None
        queue = [root]
        index = -1
        while len(reference) > 0:
            index += 1
            if queue[index] is None:
                continue
            val = reference.pop(0)
            queue[index].left = TreeNode(val) if val is not '#' else None
            queue.append(queue[index].left)
            val = reference.pop(0) if len(reference) > 0 else '#'
            queue[index].right = TreeNode(val) if val is not '#' else None
            queue.append(queue[index].right)
        return root
