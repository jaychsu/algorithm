"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param: head: The head of linked list.
    @return: You should return the head of the sorted linked list, using constant space complexity.
    """
    def sortList(self, head):
        return self.merge_sort(head)

    def quick_sort(self, head):
        if not head or not head.next:
            return head

        mid = self.find_middle(head)

        left_dummy = left_tail = ListNode(0)
        mid_dummy = mid_tail = ListNode(0)
        right_dummy = right_tail = ListNode(0)

        while head:
            if head.val < mid.val:
                left_tail.next = head
                left_tail = head
            elif head.val > mid.val:
                right_tail.next = head
                right_tail = head
            else:
                mid_tail.next = head
                mid_tail = head
            head = head.next

        left_tail.next = mid_tail.next = right_tail.next = None

        left_dummy.next = self.quick_sort(left_dummy.next)
        right_dummy.next = self.quick_sort(right_dummy.next)

        dummy = tail = ListNode(0)
        for node in [left_dummy, mid_dummy, right_dummy]:
            tail.next = node.next
            tail = self.get_tail(tail)

        return dummy.next

    def merge_sort(self, head):
        if not head or not head.next:
            return head

        left = head
        mid = self.find_middle(head)
        right = mid.next
        mid.next = None

        left = self.merge_sort(left)
        right = self.merge_sort(right)

        dummy = tail = ListNode(0)

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next

        if left:
            tail.next = left
        else:
            tail.next = right

        return dummy.next

    def find_middle(self, head):
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def get_tail(self, head):
        if not head:
            return

        while head.next:
            head = head.next

        return head
