class Solution:
    """
    maintain a set to record if there is unused cands
    """
    def longestConsecutive(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        ans = 0

        if not nums:
            return ans

        cands = set(nums)  # dedup

        for a in nums:
            if a not in cands:
                continue

            cands.discard(a)
            size = 1
            b, c = a - 1, a + 1

            while b in cands:
                cands.discard(b)
                b -= 1
                size += 1

            while c in cands:
                cands.discard(c)
                c += 1
                size += 1

            if size > ans:
                ans = size

        return ans


class Solution:
    """
    1. sorted
    2. if its consecutive, add 1 for size
    3. save the maximum size
    """
    def longestConsecutive(self, nums):
        """
        :type nums: list[int]
        :rtype: int
        """
        ans = 0

        if not nums:
            return ans

        nums.sort()

        size = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue

            if nums[i] == nums[i - 1] + 1:
                size += 1
            else:
                size = 1

            if size > ans:
                ans = size

        return ans if ans > 0 else size
