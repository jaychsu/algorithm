class Solution:
    """
    @param: A: an array
    @return: total of reverse pairs
    """
    def reversePairs(self, A):
        n = len(A)
        tmp = [0] * n
        return self.merge_sort(A, 0, n - 1, tmp)

    def merge_sort(self, A, start, end, tmp):
        if start >= end:
            return 0

        mid = (start + end) // 2
        left, right = start, mid + 1
        ans = self.merge_sort(A, left, mid, tmp)
        ans += self.merge_sort(A, right, end, tmp)

        i = start
        while left <= mid and right <= end:
            if A[left] > A[right]:
                tmp[i] = A[right]
                right += 1
                ans += mid - left + 1
            else:
                tmp[i] = A[left]
                left += 1
            i += 1

        while left <= mid:
            tmp[i] = A[left]
            left += 1
            i += 1

        while right <= end:
            tmp[i] = A[right]
            right += 1
            i += 1

        for i in range(start, end + 1):
            A[i] = tmp[i]

        return ans
