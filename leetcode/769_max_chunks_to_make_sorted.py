"""
Main Concept:
given nums: 0, 2, 1, 4, 3, 5, 7, 6

1. the sorted nums is just its index
2. maintain a `M` to record, and `M[i]` means the max in [0:i] in nums
3. if `M[i] == i`, ans += 1

sorted: 0, 1, 2, 3, 4, 5, 6, 7
index:  0, 1, 2, 3, 4, 5, 6, 7
max:    0, 2, 2, 4, 4, 5, 7, 7
ans:    1, 1, 2, 2, 3, 4, 4, 5
chunks: 0| 2, 1| 4, 3| 5| 7, 6


Improvement:

just compare when visit it
space: O(n) -> O(1)
"""


class Solution:
    def maxChunksToSorted(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        if not nums:
            return ans

        _max = 0  # since 0 is the min in nums

        for i in range(len(nums)):
            _max = max(_max, nums[i])

            if _max == i:
                ans += 1

        return ans


class Solution:
    def maxChunksToSorted(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0

        if not nums:
            return ans

        n = len(nums)
        M = [0] * n  # `M[i]` means the max in [0:i] in nums

        for i in range(n):
            M[i] = nums[i]

            if i > 0 and M[i - 1] > M[i]:
                M[i] = M[i - 1]

        for i in range(n):
            if M[i] == i:
                ans += 1

        return ans
