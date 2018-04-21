class Solution:
    """
    @param nums: the arrays
    @param k: the distance of the same number
    @return: the ans of this question
    """
    def sameNumber(self, nums, k):
        RES = ('NO', 'YES')

        if not nums or not k:
            return RES[0]

        idx = {}
        gotcha = False

        for i in range(len(nums)):
            if nums[i] in idx and i - idx[nums[i]] < k:
                gotcha = True

            idx[nums[i]] = i

        return RES[int(gotcha)]
