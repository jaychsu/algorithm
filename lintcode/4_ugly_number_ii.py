class Solution:
    """
    @param: n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        """
        this solution is very like runner

                    |<- leading runner (current last num)
        ans: [1, 2, 3, 4, 5, 6, 8, 9]
        2:    i0 i1    i2
        3:    j0    j1             j2
        5:    k0          k1         ... k2

        => min(A[i2], A[j1], A[k1]) == A[j1]
        """
        if not n:
            return 0

        ans = [1]
        c2 = c3 = c5 = 0  # count times for 2/3/5

        for i in range(1, n):
            while ans[c2] * 2 <= ans[-1]:
                c2 += 1
            while ans[c3] * 3 <= ans[-1]:
                c3 += 1
            while ans[c5] * 5 <= ans[-1]:
                c5 += 1

            ans.append(min(
                ans[c2] * 2,
                ans[c3] * 3,
                ans[c5] * 5
            ))

        return ans[-1]
