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
        new_hash = [None] * CAPACITY

        curr = tail = i = 0
        for node in hash_table:
            curr = node
            while curr:
                i = curr.val % CAPACITY

                if new_hash[i]:
                    tail = self.get_tail(new_hash[i])
                    tail.next = ListNode(curr.val)
                else:
                    new_hash[i] = ListNode(curr.val)

                curr = curr.next

        return new_hash

    def get_tail(self, head):
        if not head:
            return head

        while head.next:
            head = head.next

        return head
