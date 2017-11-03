"""
Test Case:

[2->null,null,-1->null]

[null,-1->5->11->null,null,6->10->null]

[-10->-7->-6->0->2->2->3->null,-9->null,0->1->3->3->null,-10->-9->-9->-5->-2->2->3->4->null,-9->null,-8->-6->-5->3->3->null,-10->-10->-5->-2->-1->2->2->null,4->null,-9->-5->-3->0->0->null]
: if node and node.val -> if node and isinstance(node.val, int)
: this error caused by kicked the `0` out
"""

from heapq import heappush, heappop

"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
class Solution:
    """
    @param lists: a list of ListNode
    @return: The head of one sorted list.
    """
    def mergeKLists(self, lists):
        ans = None
        if not lists:
            return ans
        parent = ans
        heap = []
        for node in lists:
            if node and isinstance(node.val, int):
                heappush(heap, (node.val, node))
        while heap:
            _, node = heappop(heap)
            if parent:
                parent.next = node
                parent = parent.next
            else:
                ans = parent = node
            if parent.next:
                heappush(heap, (parent.next.val, parent.next))
        return ans
