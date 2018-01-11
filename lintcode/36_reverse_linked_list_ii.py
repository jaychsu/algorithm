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
        if not head:
            return

        """
        to get to `n`th node from `m`th node needs `n - m` operations
        """
        n -= m

        """
        `A` will stay at `m-1`th node
        """
        A = dummy = ListNode(-1, head)
        while m > 1:
            m -= 1
            A = A.next

        """
        `B` will stay at `n+1`th node
        `cur` stay at (`m`th -> `n`th) node
        """
        B = cur = A.next
        pre = nxt = None
        while n >= 0:
            n -= 1
            nxt = B.next
            B.next = pre
            pre = B
            B = nxt

        A.next = pre
        cur.next = B

        return dummy.next
