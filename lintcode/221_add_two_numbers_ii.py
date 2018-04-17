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

        a = self.rev_list(a)
        b = self.rev_list(b)

        dummy = tail = ListNode(0)
        carry = 0

        while a and b:
            carry += a.val + b.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            a = a.next
            b = b.next
            tail = tail.next

        while a:
            carry += a.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            a = a.next
            tail = tail.next

        while b:
            carry += b.val
            tail.next = ListNode(carry % 10)
            carry //= 10
            b = b.next
            tail = tail.next

        if carry:
            tail.next = ListNode(carry)

        return self.rev_list(dummy.next)

    def rev_list(self, head):
        pre = nxt = None

        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt

        return pre
