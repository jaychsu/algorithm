class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        if not digits:
            return []

        n = len(digits)
        ans = [0] * n
        carry = 1

        for i in range(n - 1, -1, -1):
            carry += digits[i]

            ans[i] = carry % 10
            carry = carry // 10

        if carry:
            ans[:] = [1] + ans

        return ans
