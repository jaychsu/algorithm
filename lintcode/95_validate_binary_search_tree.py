"""
Main Concept:
since the fact,
if we said a tree is NOT a binary search tree,
and then the values we got by inorder traversal
is must be a non-descending sequence, that is, A[i+1] >= A[i].


Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack = []
        node = root
        pre = None

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            if pre and node.val <= pre.val:
                return False

            pre = node

            node = node.right

        return True


class Solution:
    ans = True
    pre = None

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return self.ans

        self.isValidBST(root.left)

        if self.pre and root.val <= self.pre.val:
            self.ans = False
            return self.ans

        self.pre = root

        self.isValidBST(root.right)

        return self.ans
