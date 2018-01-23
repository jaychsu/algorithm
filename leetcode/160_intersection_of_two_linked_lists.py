# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def getIntersectionNode(self, A, B):
        """
        :type A, B: ListNode
        :rtype: ListNode
        """
        if not A or not B:
            return

        X, Y = A, B

        while X and Y:
            X = X.next
            Y = Y.next

        while X:
            X = X.next
            A = A.next

        while Y:
            Y = Y.next
            B = B.next

        while A is not B:
            A = A.next
            B = B.next

        return A
