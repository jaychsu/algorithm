class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: list[int]
        :rtype: int
        """
        if not n or n <= 1 or not primes:
            return 1

        k = len(primes)

        # i -> same as `i` in `primes`, v -> track of how far `primes[i]` stay in `uglys`
        steps = [0] * k
        uglys = [0] * n
        uglys[0] = 1

        for i in range(1, n):
            ugly = float('inf')

            for j in range(k):
                ugly = min(ugly, uglys[steps[j]] * primes[j])

            uglys[i] = ugly

            for j in range(k):
                if uglys[steps[j]] * primes[j] == ugly:
                    steps[j] += 1

        return uglys[n - 1]
