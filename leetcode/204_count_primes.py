"""
REF: https://discuss.leetcode.com/topic/14036/fast-python-solution
"""


class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n or n < 3:
            return 0

        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False

        for i in range(2, int(n ** 0.5) + 1):
            if not is_prime[i]:
                continue
            for j in range(i * i, n, i):
                is_prime[j] = False

        return sum(is_prime)
