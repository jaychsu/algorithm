"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    """
    @param: A: The first list.
    @param: B: The second list.
    @return: the sum list of A and B.
    """
    def addLists2(self, A, B):
        if not A:
            return B
        if not B:
            return A

        A = self.reverse_list(A)
        B = self.reverse_list(B)

        dummy = tail = ListNode(-1)
        _carry = 0

        while A and B:
            _carry += A.val + B.val
            tail.next = ListNode(_carry % 10)
            tail = tail.next
            A = A.next
            B = B.next
            _carry //= 10

        while A:
            _carry += A.val
            tail.next = ListNode(_carry % 10)
            tail = tail.next
            A = A.next
            _carry //= 10

        while B:
            _carry += B.val
            tail.next = ListNode(_carry % 10)
            tail = tail.next
            B = B.next
            _carry //= 10

        if _carry > 0:
            tail.next = ListNode(_carry)

        return self.reverse_list(dummy.next)

    def reverse_list(self, head):
        pre = nxt = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre
