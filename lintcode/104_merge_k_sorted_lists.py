"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
import heapq


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: list[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return

        dummy = tail = ListNode(-1)
        heap = []

        for i in range(len(lists)):
            if not lists[i]:
                continue

            heapq.heappush(heap, (lists[i].val, i))

        while heap:
            val, i = heapq.heappop(heap)

            tail.next = ListNode(val)
            tail = tail.next

            if lists[i].next:
                lists[i] = lists[i].next
                heapq.heappush(heap, (lists[i].val, i))

        return dummy.next
