class Solution:
    def largestDivisibleSubset(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        ans = []
        if not A:
            return ans

        n = len(A)
        if n == 1:
            return A

        A.sort()

        """
        this problem similar with LIS

        `dp[i]` means the maximum size of subset end at `i`
        note that there is size, so init with `1`

        `pi[i]` records the previous num in ans, and allow to backtrack
        to find all num in ans

        `pe` means path end, to record the LDS end
        """
        dp = [1] * n
        pi = [0] * n
        pe = max_size = 0

        for i in range(n):
            for j in range(i):
                """
                backtracking

                `A[i]` is larger than `A[j]`,
                so check `A[i] % A[j]` if its zero
                """
                if A[i] % A[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    pi[i] = j

                if dp[i] > max_size:
                    max_size = dp[i]
                    pe = i

        ans = [0] * max_size
        for i in range(max_size - 1, -1, -1):
            ans[i] = A[pe]
            pe = pi[pe]

        return ans
