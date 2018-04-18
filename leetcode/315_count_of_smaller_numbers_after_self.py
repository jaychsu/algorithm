class Solution:
    """
    REF: https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76657/
    """
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []

        n = len(nums)
        ans = [0] * n

        cands = sorted(set(nums))
        v2i = {cands[i]: i for i in range(len(cands))}
        self.bits = [0] * (len(v2i) + 1)

        for i in range(n - 1, -1, -1):
            j = v2i[nums[i]]
            ans[i] = self.sum(j)
            self.update(j)

        return ans

    def update(self, i):
        i += 1

        while i < len(self.bits):
            self.bits[i] += 1
            i += (i & -i)

    def sum(self, i):
        res = 0

        while i > 0:
            res += self.bits[i]
            i -= (i & -i)

        return res


class Solution:
    """
    Brute Force: TLE
    """
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
