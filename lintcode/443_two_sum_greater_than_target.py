class Solution:
    """
    @param: A: an array of integer
    @param: target: An integer
    @return: an integer
    """
    def twoSum2(self, A, target):
        if not A or len(A) < 2:
            return 0

        A.sort()

        left, right = 0, len(A) - 1
        ans = 0
        while left < right:
            # if minimum + maximum still <= target
            # ignore the 2nd, 3rd maximum
            if A[left] + A[right] <= target:
                left += 1
                continue

            # if minimum + maximum > target
            # we can ensure the 2nd, 3rd minimum also fit demand
            ans += right - left
            right -= 1

        return ans
