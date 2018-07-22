from traversal.python._helper import *


class IterativeTraversal(TraversalBase):
    @classmethod
    def preorder_traverse(cls, root, callback=None):
        """
        :type root: TreeNode
        :type callback: function
        :rtype: void
        """
        node = root
        stack = []

        while node or stack:
            while node:
                callback(node.val)
                stack.append(node)
                node = node.left

            node = stack.pop()
            node = node.right

    @classmethod
    def inorder_traverse(cls, root, callback=None):
        """
        :type root: TreeNode
        :type callback: function
        :rtype: void
        """
        node = root
        stack = []

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()
            callback(node.val)
            node = node.right

    @classmethod
    def postorder_traverse(cls, root, callback=None):
        """
        :type root: TreeNode
        :type callback: function
        :rtype: void
        """
        node = last_visit = root
        stack = []

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack[-1]

            if node.right and last_visit is not node.right:
                node = node.right
            else:
                stack.pop()

                callback(node.val)
                last_visit = node
                node = None
