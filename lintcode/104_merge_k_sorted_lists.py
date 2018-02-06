# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from heapq import heappush, heappop


class Solution:
    def mergeKLists(self, L):
        """
        :type L: List[ListNode]
        :rtype: ListNode
        """
        if not L:
            return

        heap = []
        dummy = tail = ListNode(-1)

        for i in range(len(L)):
            if not L[i]:
                continue
            heappush(heap, (L[i].val, i))

        while heap:
            val, i = heappop(heap)

            tail.next = ListNode(val)
            tail = tail.next

            L[i] = L[i].next
            if not L[i]:
                continue
            heappush(heap, (L[i].val, i))

        return dummy.next
