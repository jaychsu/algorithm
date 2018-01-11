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
            pre: None
            nxt: None
        r1:
            head: 2
            pre: 1
            nxt: 2->3
        r2:
            head: 3
            pre: 2->1
            nxt: 3
        r3:
            head: None
            pre: 3->2->1
            nxt: None
        """
        pre = nxt = None

        while head:
            nxt = head.next  # save the remaining children
            head.next = pre  # break the link
            pre = head       # save the new head
            head = nxt       # pointer the old head

        return pre
