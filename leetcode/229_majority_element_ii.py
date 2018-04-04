class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []

        if not nums:
            return []

        a1 = a2 = None
        c1 = c2 = 0

        for num in nums:
            if a1 == num:
                c1 += 1
            elif a2 == num:
                c2 += 1
            elif c1 == 0:
                a1, c1 = num, 1
            elif c2 == 0:
                a2, c2 = num, 1
            else:
                c1 -= 1
                c2 -= 1

        c1 = c2 = 0

        for num in nums:
            if num == a1:
                c1 += 1
            elif num == a2:
                c2 += 1

        for a, c in ((a1, c1), (a2, c2)):
            if c > len(nums) // 3:
                ans.append(a)

        return ans
