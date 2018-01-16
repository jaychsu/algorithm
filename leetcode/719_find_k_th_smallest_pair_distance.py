class Solution:
    def smallestDistancePair(self, A, k):
        """
        :type A: List[int]
        :type k: int
        :rtype: int
        """
        if not A or not k:
            return -1

        A.sort()

        left, right = 0, A[-1] - A[0]
        while left + 1 < right:
            mid = (left + right) // 2
            if self.check_valid(A, mid, k):
                right = mid
            else:
                left = mid

        return left if self.check_valid(A, left, k) else right

    def check_valid(self, A, mid, k):
        """
        valid if there are at least `k` pairs when distance is `mid`
        """
        cnt = left = 0

        for right in range(len(A)):
            while A[right] - A[left] > mid:
                left += 1

            cnt += right - left

            if cnt >= k:
                return True

        return False
