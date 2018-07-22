from traversal.python._helper import *
from tree.python import TreeNode


class MorrisTraversal(TraversalBase):
    """
    REF: https://www.cnblogs.com/AnnieKim/archive/2013/06/15/MorrisTraversal.html
    """

    @classmethod
    def preorder_traverse(cls, root, callback=None):
        """
        :type root: TreeNode
        :type callback: function
        :rtype: void
        """
        node = None

        while root:
            if not root.left:
                callback(root.val)
                root = root.right
                continue

            node = root.left

            while node.right and node.right is not root:
                node = node.right

            if node.right:
                node.right = None
                root = root.right
            else:
                callback(root.val)
                node.right = root
                root = root.left

    @classmethod
    def inorder_traverse(cls, root, callback=None):
        """
        :type root: TreeNode
        :type callback: function
        :rtype: void
        """
        node = None

        while root:
            if not root.left:
                callback(root.val)
                root = root.right
                continue

            node = root.left

            while node.right and node.right is not root:
                node = node.right

            if node.right:
                callback(root.val)
                node.right = None
                root = root.right
            else:
                node.right = root
                root = root.left

    @classmethod
    def postorder_traverse(cls, root, callback=None):
        """
        :type root: TreeNode
        :type callback: function
        :rtype: void
        """
        dummy = TreeNode(0)
        dummy.left = root

        root = dummy
        node = None

        while root:
            if not root.left:
                root = root.right
                continue

            node = root.left

            while node.right and node.right is not root:
                node = node.right

            if node.right:
                cls._postorder_reverse_visit(root.left, node, callback=callback)
                node.right = None
                root = root.right
            else:
                node.right = root
                root = root.left

    @classmethod
    def _postorder_reverse_visit(cls, from_node, to_node, callback):
        cls._postorder_reverse(from_node, to_node)

        node = to_node
        callback(node.val)

        while node and node is not from_node:
            node = node.right
            callback(node.val)

        cls._postorder_reverse(to_node, from_node)

    @classmethod
    def _postorder_reverse(cls, from_node, to_node):
        root = from_node
        node = from_node.right
        nxt = None

        while root is not to_node:
            nxt = node.right
            node.right = root
            root = node
            node = nxt
