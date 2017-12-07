"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: node: a list node in the list
    @param: x: An integer
    @return: the inserted new list node
    """
    def insert(self, node, x):
        if not node:
            node = ListNode(x)
            node.next = node
            return node

        pre, cur = None, node
        while True:
            pre = cur
            cur = cur.next

            # in the list
            if pre.val <= x <= cur.val:
                break

            # at the boundary between minimum and maximum
            if (pre.val > cur.val) and (x < cur.val or x > pre.val):
                break

            # if `cur` have already traversed the list once
            if cur is node:
                break

        new_node = ListNode(x)
        new_node.next = cur
        pre.next = new_node
        return new_node
