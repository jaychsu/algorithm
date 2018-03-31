class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums or len(nums) < 3 or target is None:
            return -1

        ans = INF = float('inf')
        n = len(nums)
        nums.sort()

        for a in range(n - 2):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            b, c = a + 1, n - 1

            while b < c:
                total = nums[a] + nums[b] + nums[c]

                if total == target:
                    return total

                if abs(total - target) < abs(ans - target):
                    ans = total

                if total < target:
                    b += 1
                else:
                    c -= 1

        return ans if ans < INF else -1
