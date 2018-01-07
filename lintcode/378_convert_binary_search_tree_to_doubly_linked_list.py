"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None

Definition of Doubly-ListNode
class DoublyListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = self.prev = next
"""


class Solution:
    """
    @param: root: The root of tree
    @return: the head of doubly list node
    """
    def bstToDoublyList(self, root):
        if not root:
            return

        dummy = tail = DoublyListNode(-1)
        stack = []
        node = root

        while node or stack:
            while node:
                stack.append(node)
                node = node.left

            node = stack.pop()

            _node = DoublyListNode(node.val)
            _node.prev = tail
            tail.next = _node
            tail = tail.next

            node = node.right

        return dummy.next
