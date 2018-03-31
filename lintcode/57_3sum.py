class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []

        if not nums or len(nums) < 3:
            return ans

        n = len(nums)
        nums.sort()

        for a in range(n - 2):
            if a > 0 and nums[a] == nums[a - 1]:
                continue

            b, c = a + 1, n - 1

            while b < c:
                total = nums[a] + nums[b] + nums[c]

                if total == 0:
                    ans.append([nums[a], nums[b], nums[c]])
                    b += 1
                    c -= 1
                    while b < c and nums[b] == nums[b - 1]:
                        b += 1
                    while b < c and nums[c] == nums[c + 1]:
                        c -= 1
                elif total < 0:
                    b += 1
                else:
                    c -= 1

        return ans
