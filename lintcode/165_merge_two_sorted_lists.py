"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    def mergeTwoLists(self, A, B):
        """
        :type A: ListNode
        :type B: ListNode
        :rtype: ListNode
        """
        dummy = tail = ListNode(-1)

        while A and B:
            if A.val < B.val:
                tail.next = ListNode(A.val)
                A = A.next
            else:
                tail.next = ListNode(B.val)
                B = B.next
            tail = tail.next

        while A:
            tail.next = ListNode(A.val)
            A = A.next
            tail = tail.next

        while B:
            tail.next = ListNode(B.val)
            B = B.next
            tail = tail.next

        return dummy.next
