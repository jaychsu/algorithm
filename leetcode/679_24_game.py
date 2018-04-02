class Solution:
    EPS = 1e-6
    OP = (
        lambda a, b: a + b,
        lambda a, b: a * b,
        lambda a, b: a - b,
        lambda a, b: a / b,
    )

    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        n = len(nums)

        if n == 1:
            return abs(nums[0] - 24) < self.EPS

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                nxts = [nums[k] for k in range(n) if i != k != j]  # i != j != k is different

                for k in range(len(self.OP)):
                    if i < j and k < 2:
                        # since a + b == b + a, so just do half in j >= i
                        # same for `*`
                        continue
                    if nums[j] == 0 and k == 3:
                        # divide by 0
                        continue

                    nxts.append(self.OP[k](nums[i], nums[j]))

                    if self.judgePoint24(nxts):
                        return True

                    nxts.pop()

        return False
