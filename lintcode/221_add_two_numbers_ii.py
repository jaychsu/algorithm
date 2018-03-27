"""
Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
"""


class Solution:
    def addLists2(self, a, b):
        """
        :type a: ListNode
        :type b: ListNode
        :rtype: ListNode
        """
        if not a and not b:
            return
        if not a:
            return b
        if not b:
            return a

        a = self.reverse_list(a)
        b = self.reverse_list(b)

        carry = 0
        dummy = tail = ListNode(-1)

        while a and b:
            carry += a.val + b.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            tail = tail.next
            a = a.next
            b = b.next

        while a:
            carry += a.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            tail = tail.next
            a = a.next

        while b:
            carry += b.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            tail = tail.next
            b = b.next

        if carry:
            tail.next = ListNode(carry)

        return self.reverse_list(dummy.next)

    def reverse_list(self, head):
        cur = nxt = None

        while head:
            nxt = head.next
            head.next = cur
            cur = head
            head = nxt

        return cur
