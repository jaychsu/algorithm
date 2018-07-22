from abc import ABC, abstractmethod


class TraversalBase(ABC):
    @classmethod
    @abstractmethod
    def preorder_traverse(cls, root, callback=None):
        """
        :type root: TreeNode
        :type callback: function
        :rtype: void
        """
        pass

    @classmethod
    @abstractmethod
    def inorder_traverse(cls, root, callback=None):
        """
        :type root: TreeNode
        :type callback: function
        :rtype: void
        """
        pass

    @classmethod
    @abstractmethod
    def postorder_traverse(cls, root, callback=None):
        """
        :type root: TreeNode
        :type callback: function
        :rtype: void
        """
        pass
