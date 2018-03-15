class Solution:
    def lastRemaining(self, n):
        """
        :type n: int
        :rtype: int
        """
        ans = gap = 1
        turn = 0

        while n > 1:
            turn += 1
            n //= 2
            gap *= 2
            delta = gap // 2 + gap * (n - 1)

            if turn & 1:
                ans += delta
            else:
                ans -= delta

        return ans
