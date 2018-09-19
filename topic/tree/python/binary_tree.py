class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


class BinaryTree:
    EMPTY = '#'
    TMPL = '{{{}}}'  # {{, }} is to escape brackets

    @classmethod
    def serialize(cls, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return cls.TMPL.format('')

        values = []
        queue = [root]

        for node in queue:
            if not node:
                values.append(cls.EMPTY)
                continue

            values.append(str(node.val))
            queue.append(node.left)
            queue.append(node.right)

        while values[-1] == cls.EMPTY:
            values.pop()

        return cls.TMPL.format(','.join(values))

    @classmethod
    def deserialize(cls, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if any((
            not data,
            len(data) < 3,
            data[0] != '{',
            data[-1] != '}',
            data[1] in (cls.EMPTY, ','),
        )):
            return

        values = data[1:-1].split(',')
        i = 0
        root = TreeNode(int(values[i]))
        queue = [root]

        for node in queue:
            for branch in ('left', 'right'):
                i += 1

                if i >= len(values):
                    break
                if values[i] == cls.EMPTY:
                    continue

                setattr(node, branch, TreeNode(int(values[i])))
                queue.append(getattr(node, branch))

        return root
