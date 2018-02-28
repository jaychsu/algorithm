# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, a, b):
        """
        :type a: ListNode
        :type b: ListNode
        :rtype: ListNode
        """
        dummy = tail = ListNode(-1)

        while a and b:
            if a.val < b.val:
                tail.next = ListNode(a.val)
                a = a.next
            else:
                tail.next = ListNode(b.val)
                b = b.next
            tail = tail.next

        while a:
            tail.next = ListNode(a.val)
            a = a.next
            tail = tail.next

        while b:
            tail.next = ListNode(b.val)
            b = b.next
            tail = tail.next

        return dummy.next
