"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        """
        example: 1->2->3

        r0:
            head: 1
            _head: None
            remaining: None
        r1:
            head: 2
            _head: 1
            remaining: 2->3
        r2:
            head: 3
            _head: 2->1
            remaining: 3
        r3:
            head: None
            _head: 3->2->1
            remaining: None
        """
        _head = remaining = None
        while head:
            remaining = head.next  # save the remaining children
            head.next = _head      # break the link
            _head = head           # save the new head
            head = remaining       # pointer the old head
        return _head
