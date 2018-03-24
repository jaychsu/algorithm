class Solution:
    def computeLastDigit(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if not a or not b:
            return 0
        if a == b:
            return 1

        ans = 1

        for num in range(a + 1, b + 1):
            if ans == 0:
                return 0

            ans *= num % 10
            ans %= 10

        return ans
