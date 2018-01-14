class Solution:
    """
    @param: k: An integer
    @param: n: An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        ans = 0
        for i in range(n + 1):
            ans += self.count(k, i)
        return ans

    def count(self, k, a):
        if k == a == 0:
            return 1

        cnt = 0
        while a:
            if a % 10 == k:
                cnt += 1
            a //= 10
        return cnt
