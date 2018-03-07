class Solution:
    def mergeSortedArray(self, a, m, b, n):
        """
        :type a: List[int]
        :type m: int
        :type b: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if a[i] > b[j]:
                a[k] = a[i]
                i -= 1
            else:
                a[k] = b[j]
                j -= 1
            k -= 1

        while j >= 0:
            a[k] = b[j]
            j -= 1
            k -= 1
