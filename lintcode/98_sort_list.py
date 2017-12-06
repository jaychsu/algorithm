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
        pass

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
