class Solution:
    def wiggleSort(self, A):
        """
        :type A: List[int]
        :rtype: void Do not return anything, modify A in-place instead.
        """
        if not A:
            return

        for i in range(1, len(A)):
            if i & 1 == 1 and A[i] >= A[i - 1]:
                continue
            if i & 1 == 0 and A[i] <= A[i - 1]:
                continue
            A[i], A[i - 1] = A[i - 1], A[i]
