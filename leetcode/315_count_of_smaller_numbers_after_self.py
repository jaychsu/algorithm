"""
REF: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76657/
"""
class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        if not nums:
            return ans

        v2i = {v: i for i, v in enumerate(sorted(set(nums)))}
        self.bits = [0] * (len(v2i) + 1)

        for i in range(len(nums) - 1, -1, -1):
            j = v2i[nums[i]]

            ans.append(self.sum(j))
            self.update(j + 1)

        return ans[::-1]

    def update(self, i, delta=1):
        while i < len(self.bits):
            self.bits[i] += delta
            i += (i & -i)

    def sum(self, i):
        res = 0

        while i > 0:
            res += self.bits[i]
            i -= (i & -i)

        return res


"""
Brute Force: TLE
"""
class Solution:
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        if not nums:
            return ans

        n = len(nums)

        for i in range(n):
            ans.append(0)

            for j in range(i, n):
                if nums[j] < nums[i]:
                    ans[-1] += 1

        return ans
