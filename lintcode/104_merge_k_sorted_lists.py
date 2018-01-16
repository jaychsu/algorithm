# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from heapq import heappop, heappush


class Solution:
    def mergeKLists(self, L):
        """
        :type L: List[ListNode]
        :rtype: ListNode
        """
        if not L:
            return

        heap = []
        for i in range(len(L)):
            if not L[i]:
                continue
            heappush(heap, (L[i].val, i))

        dummy = tail = ListNode(-1)
        while heap:
            val, i = heappop(heap)
            tail.next = ListNode(val)
            tail = tail.next
            L[i] = L[i].next
            if L[i]:
                heappush(heap, (L[i].val, i))

        return dummy.next
