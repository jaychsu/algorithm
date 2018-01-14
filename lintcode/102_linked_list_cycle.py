"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The first node of linked list.
    @return: True if it has a cycle, or false
    """
    def hasCycle(self, head):
        """
        if its a cycle, and then we can ensure
        the 2-pace pointer and the 1-pace pointer
        will eventually meet
        otherwise its a list => at some point there will be no `node.next`
        """
        if not head or not head.next:
            return False

        slow = head
        fast = head.next
        while slow != fast:
            if not fast.next or not fast.next.next:
                return False

            slow = slow.next
            fast = fast.next.next

        return True
