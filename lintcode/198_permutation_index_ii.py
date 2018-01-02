"""
https://segmentfault.com/a/1190000004683277

if there are `dups`, dividing `factorial` with `dup_fact`
e.g., 3 `A[i]`s and 4 `A[j]`s in `A`
`dup_fact = 3! * 4!`
"""


class Solution:
    """
    @param: A: An array of integers
    @return: A long integer
    """
    def permutationIndexII(self, A):
        ans = 1
        if not A:
            return ans

        n = len(A)
        factorial = dup_fact = 1
        dups = {}

        for i in range(n - 1, -1, -1):
            dups[A[i]] = dups.get(A[i], 0) + 1
            dup_fact *= dups[A[i]]

            cnt = 0
            for j in range(i + 1, n):
                if A[i] > A[j]:
                    cnt += 1

            ans += cnt * factorial // dup_fact
            factorial *= n - i

        return ans
