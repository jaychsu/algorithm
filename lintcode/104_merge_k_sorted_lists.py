"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
from heapq import heappop, heappush


class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        if not lists:
            return

        dummy = tail = ListNode(-1)
        candidates = []
        for node in lists:
            if node:
                heappush(candidates, (node.val, node))

        while candidates:
            _, node = heappop(candidates)
            tail.next = node
            tail = tail.next

            if node.next:
                heappush(candidates, (node.next.val, node.next))

        return dummy.next
