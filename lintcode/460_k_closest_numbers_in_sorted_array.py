class Solution:
    """
    @param: A: an integer array
    @param: target: An integer
    @param: k: An integer
    @return: an integer array
    """
    def kClosestNumbers(self, A, target, k):
        if not A:
            return []

        n = len(A)

        """
        if `b` in `A`:
            [a, b, b, b, c]
                      l  r
        else:
            [a, c, d, e, f]
             l  r
        """
        left, mid, right = 0, 0, n - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if A[mid] <= target:
                left = mid
            else:
                right = mid

        """
        # handle out of range
        if `left` less than `0`
            only append `A[right]`
        if `right` great than `n - 1`
            only append `A[left]`

        # handle closest
        append first if that `num` is more closer `target`
        """
        ans = [0] * k
        for i in range(k):
            if left < 0:
                ans[i] = A[right]
                right += 1
            elif right >= n:
                ans[i] = A[left]
                left -= 1
            elif A[right] - target < target - A[left]:
                ans[i] = A[right]
                right += 1
            else:
                ans[i] = A[left]
                left -= 1

        return ans
