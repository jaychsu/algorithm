class Solution:
    """
    @param: A: Give an array A of n integer
    @param: target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, A, target):
        if not A or len(A) < 3:
            return

        A.sort()

        INFINITY = float('inf')
        n = len(A)
        b = c = _sum = 0
        ans = INFINITY
        for a in range(n - 2):
            b = a + 1
            c = n - 1
            while b < c:
                _sum = A[a] + A[b] + A[c]
                if abs(_sum - target) < abs(ans - target):
                    ans = _sum
                if _sum <= target:
                    b += 1
                else:
                    c -= 1

        return ans if ans < INFINITY else None
