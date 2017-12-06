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

        left_dummy, right_dummy = ListNode(0), ListNode(0)
        left_end, right_end = left_dummy, right_dummy

        while head:
            if head.val < x:
                left_end.next = head
                left_end = head
            else:
                right_end.next = head
                right_end = head
            head = head.next

        right_end.next = None
        left_end.next = right_dummy.next
        return left_dummy.next
