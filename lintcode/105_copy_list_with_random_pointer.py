"""
Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
"""


"""
using hashmap
time: O(2n) => O(n)
space: O(n)
"""
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        dummy = dummy_end = RandomListNode(-1)
        new_node = None
        indices = {}

        """
        copy the origin main list
        and temply save origin random node
        """
        while head:
            new_node = RandomListNode(head.label)
            new_node.random = head.random
            dummy_end.next = new_node
            indices[head] = new_node

            dummy_end = dummy_end.next
            head = head.next

        """
        iterate the new list
        and replace the random node in new list
        """
        head = dummy.next
        while head:
            if head.random:
                head.random = indices[head.random]
            head = head.next

        return dummy.next


"""
temply save in n.next
time: O(3n) => O(n)
space: O(1)
"""
class Solution:
    # @param head: A RandomListNode
    # @return: A RandomListNode
    def copyRandomList(self, head):
        """
        example: 1->2->3

        copy_next/
            |--------->|
            1 -> 1' -> 2 -> 2' -> 3 -> 3'
        replace_random/
                 |--------->|
            |----+---->|    |
            1 -> 1' -> 2 -> 2' -> 3 -> 3'
        split_list/
            |--------->|
            1    ->    2    ->    3
                 1'   ->    2'   ->    3'
                 |--------->|
        """
        if not head:
            return

        self.copy_next(head)
        self.replace_random(head)
        return self.split_list(head)

    def copy_next(self, head):
        new_node = None

        while head:
            new_node = RandomListNode(head.label)
            new_node.random = head.random
            new_node.next = head.next
            head.next = new_node

            head = head.next.next

    def replace_random(self, head):
        while head:
            if head.next and head.random:
                head.next.random = head.random.next

            head = head.next.next

    def split_list(self, head):
        dummy = dummy_end = head.next

        while head:
            dummy_end = head.next
            head.next = dummy_end.next
            if dummy_end.next:
                dummy_end.next = dummy_end.next.next

            head = head.next

        return dummy
