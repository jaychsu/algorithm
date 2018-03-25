class Solution:
    def PalindromicRanges(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        if left > right:
            return 0
        if left == right:
            return 1

        dp = [0] * (right - left + 2)  # n + 1, n = right - left + 1
        # dp[0] = 0

        for num in range(left, right + 1):
            if self.is_palindrome(num):
                dp[num - left + 1] = dp[num - left] + 1
            else:
                dp[num - left + 1] = dp[num - left]

        ans = 0

        for i in range(1, right - left + 2):
            for j in range(i):
                if ((dp[i] - dp[j]) & 1 == 0):
                    ans += 1

        return ans

    def is_palindrome(self, num):
        if num // 10 == 0:
            return True

        s = str(num)
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
