from traversal.python._helper import *


class RecursiveTraversal(TraversalBase):
    @classmethod
    def preorder_traverse(cls, root, callback=None):
        """
        :type root: TreeNode
        :type callback: function
        :rtype: void
        """
        if not root:
            return

        callback(root.val)
        cls.preorder_traverse(root.left, callback=callback)
        cls.preorder_traverse(root.right, callback=callback)

    @classmethod
    def inorder_traverse(cls, root, callback=None):
        """
        :type root: TreeNode
        :type callback: function
        :rtype: void
        """
        if not root:
            return

        cls.inorder_traverse(root.left, callback=callback)
        callback(root.val)
        cls.inorder_traverse(root.right, callback=callback)

    @classmethod
    def postorder_traverse(cls, root, callback=None):
        """
        :type root: TreeNode
        :type callback: function
        :rtype: void
        """
        if not root:
            return

        cls.postorder_traverse(root.left, callback=callback)
        cls.postorder_traverse(root.right, callback=callback)
        callback(root.val)
