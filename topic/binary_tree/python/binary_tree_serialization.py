from collections import deque


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class BinaryTree:
    NULL_NODE = '#'

    @classmethod
    def serialize(cls, root):
        if not isinstance(root, TreeNode):
            return '{}'

        queue = [root]
        values = []

        for node in queue:
            if not node:
                values.append(cls.NULL_NODE)
                continue

            queue.append(node.left)
            queue.append(node.right)
            values.append(str(node.val))

        while values[-1] == cls.NULL_NODE:
            values.pop()

        return '{%s}' % ','.join(values)

    @classmethod
    def deserialize(cls, data):
        if not isinstance(data, str) \
                or data[0] != '{' \
                or data[-1] != '}':
            return

        values = deque(data[1:-1].split(','))
        if not values:
            return
        value = values.popleft()
        if value == cls.NULL_NODE:
            return

        root = TreeNode(int(value))
        queue = [root]

        for node in queue:
            # add to left child
            if not values:
                break
            value = values.popleft()
            if value != cls.NULL_NODE:
                node.left = TreeNode(int(value))
                queue.append(node.left)

            # add to right child
            if not values:
                break
            value = values.popleft()
            if value != cls.NULL_NODE:
                node.right = TreeNode(int(value))
                queue.append(node.right)

        return root
