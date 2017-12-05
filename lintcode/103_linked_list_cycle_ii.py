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
    @return: The node where the cycle begins. if there is no cycle, return null
    """
    def detectCycle(self, head):
        """
        example: 1->2->3
                    ^  v
                    5<-4

        * h: head, l: left, r: right, i: intersection node

        r1/
            l    r
            1 -> 2 -> 3
                 ^    v
                 5 <- 4

        r2/
                 l
            1 -> 2 -> 3
                 ^    v
                 5 <- 4  r

        r3/
                 r    l
            1 -> 2 -> 3
                 ^    v
                 5 <- 4

        r4/
            h    i
            1 -> 2 -> 3
                 ^    v
                 5 <- 4  l, r

        h->i == 1
        l->i == 2
        """
        if not head or not head.next:
            return

        """
        if its a cycle, and then we can ensure
        the 2-pace pointer and the 1-pace pointer
        will eventually meet
        otherwise its a list => at some point there will be no `node.next`
        """
        left, right = head, head.next
        while left != right:
            if not right or not right.next:
                return
            left = left.next
            right = right.next.next

        """
        at this point, left meet right
        and at the intersection node
        the steps from the first node is equal to from meet node plus 1
        """
        while head != left.next:
            head = head.next
            left = left.next

        return head
