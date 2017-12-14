"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param hash_table: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def rehashing(self, hash_table):
        if not hash_table:
            return

        CAPACITY = len(hash_table) * 2
        heads = [None] * CAPACITY
        tails = [None] * CAPACITY

        curr = _node = i = None
        for node in hash_table:
            curr = node

            while curr:
                i = curr.val % CAPACITY
                _node = ListNode(curr.val)

                if heads[i]:
                    tails[i].next = _node
                else:
                    heads[i] = _node

                tails[i] = _node

                curr = curr.next

        return heads
