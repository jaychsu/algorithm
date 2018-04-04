"""
Main Concept:

1. start from 1 => `ans = [1]`
2. use `i2, i3, i5` to record current used in `ans`
3. if the candidates is not ahead `ans[-1]`, move forward
4. append the minimum candidate to `ans`
"""


class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if not n:
            return 0

        ans = [1]
        i2 = i3 = i5 = 0

        for _ in range(1, n):
            while ans[i2] * 2 <= ans[-1]:
                i2 += 1
            while ans[i3] * 3 <= ans[-1]:
                i3 += 1
            while ans[i5] * 5 <= ans[-1]:
                i5 += 1

            ans.append(min((
                ans[i2] * 2,
                ans[i3] * 3,
                ans[i5] * 5,
            )))

        return ans[-1]
