class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []

        if not nums or len(nums) < 4 or target is None:
            return ans

        n = len(nums)
        nums.sort()

        for a in range(n - 3):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            for b in range(a + 1, n - 2):
                if b > a + 1 and nums[b] == nums[b - 1]:
                    continue

                c, d = b + 1, n - 1

                while c < d:
                    total = nums[a] + nums[b] + nums[c] + nums[d]

                    if total == target:
                        ans.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c - 1]:
                            c += 1
                        while c < d and nums[d] == nums[d + 1]:
                            d -= 1
                    elif total < target:
                        c += 1
                    else:
                        d -= 1

        return ans
