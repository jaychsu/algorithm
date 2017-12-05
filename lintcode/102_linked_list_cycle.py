"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        """
        if its a cycle, and then we can ensure
        the 2-pace pointer and the 1-pace pointer
        will eventually meet
        otherwise its a list => at some point there will be no `node.next`
        """
        if not head or not head.next:
            return False

        left, right = head, head.next
        while left != right:
            if not right or not right.next:
                return False
            left = left.next
            right = right.next.next

        return True
