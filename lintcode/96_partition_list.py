"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list
    @param: x: An integer
    @return: A ListNode
    """
    def partition(self, head, x):
        if not head:
            return

        left_dummy = left_tail = ListNode(-1)
        right_dummy = right_tail = ListNode(-1)

        while head:
            node = ListNode(head.val)
            if head.val < x:
                left_tail.next = node
                left_tail = node
            else:
                right_tail.next = node
                right_tail = node
            head = head.next

        left_tail.next = right_dummy.next
        return left_dummy.next
