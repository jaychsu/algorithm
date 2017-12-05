"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: ListNode head is the head of the linked list
    @param: m: An integer
    @param: n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        """
        example: 1->2->3->4->5
        reverse [3,4]
        * mp: mth_pre, m: mth, n: nth, nn: nth_nxt

        init/
        dummy -> 1 -> 2 -> 3 -> 4 -> 5 -> None
                      mp   m    n    nn

        reverse/
        dummy -> 1 -> 2  | 4 -> 3 |  5 -> None
                      mp   n    m    nn

        re-link/
        dummy -> 1 -> 2 -> 4 -> 3 -> 5 -> None
                      mp   n    m    nn
        """
        dummy = ListNode(-1, head)
        mth_pre = self.find_kth(dummy, m - 1)
        mth = mth_pre.next
        nth = self.find_kth(dummy, n)
        nth_nxt = nth.next
        nth.next = None

        self.reverse(mth)
        mth_pre.next = nth
        mth.next = nth_nxt
        return dummy.next

    def find_kth(self, head, k):
        for i in range(k):
            if not head:
                return
            head = head.next
        return head

    def reverse(self, head):
        pre = nxt = None
        while head:
            nxt = head.next
            head.next = pre
            pre = head
            head = nxt
        return pre
