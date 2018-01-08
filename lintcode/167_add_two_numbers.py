"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: A: the first list
    @param: B: the second list
    @return: the sum list of A and B
    """
    def addLists(self, A, B):
        dummy = tail = ListNode(-1)
        _carry = _sum = 0

        while A and B:
            _sum = A.val + B.val + _carry
            _carry = _sum // 10 if _sum >= 10 else 0
            tail.next = ListNode(_sum % 10)
            A = A.next
            B = B.next
            tail = tail.next

        while A:
            _sum = A.val + _carry
            _carry = _sum // 10 if _sum >= 10 else 0
            tail.next = ListNode(_sum % 10)
            A = A.next
            tail = tail.next

        while B:
            _sum = B.val + _carry
            _carry = _sum // 10 if _sum >= 10 else 0
            tail.next = ListNode(_sum % 10)
            B = B.next
            tail = tail.next

        if _carry > 0:
            tail.next = ListNode(_carry)

        return dummy.next
