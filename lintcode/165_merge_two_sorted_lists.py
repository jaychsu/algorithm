"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: l1: ListNode l1 is the head of the linked list
    @param: l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(-1)
        dummy_end = dummy

        while l1 and l2:
            if l1.val < l2.val:
                dummy_end.next = l1
                l1 = l1.next
            else:
                dummy_end.next = l2
                l2 = l2.next
            dummy_end = dummy_end.next

        if l1:
            dummy_end.next = l1
        else:
            dummy_end.next = l2

        return dummy.next
