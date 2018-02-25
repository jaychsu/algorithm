class Solution:
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        ans = 0

        for i in range(1, N + 1):
            if self.is_good(i):
                ans += 1

        return ans

    def is_good(self, N):
        res = False

        while N > 0:
            D = N % 10
            if D in (3, 4, 7):
                return False
            if D in (2, 5, 6, 9):
                res = True
            N = N // 10

        return res
