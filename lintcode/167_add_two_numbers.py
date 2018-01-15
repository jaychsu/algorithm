"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    def addLists(self, A, B):
        """
        :type A: ListNode
        :type B: ListNode
        :rtype: ListNode
        """
        dummy = tail = ListNode(-1)
        carry = 0

        while A and B:
            carry += A.val + B.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            tail = tail.next
            A = A.next
            B = B.next

        while A:
            carry += A.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            tail = tail.next
            A = A.next

        while B:
            carry += B.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            tail = tail.next
            B = B.next

        if carry:
            tail.next = ListNode(carry)

        return dummy.next
