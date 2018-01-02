"""
https://segmentfault.com/a/1190000004683277

in the origin/unsorted `A`,
if there are `cnt` child after and less than `A[i]`,
meaning there are `cnt * (n - i - 1)!` permutations
before `A[i]`.
"""


class Solution:
    """
    @param: A: An array of integers
    @return: A long integer
    """
    def permutationIndex(self, A):
        ans = 1
        if not A:
            return ans

        n = len(A)
        factorial = 1

        for i in range(n - 1, -1, -1):
            cnt = 0
            for j in range(i + 1, n):
                if A[i] > A[j]:
                    cnt += 1

            """
            use the `factorial` from previous iteration `i + 1`
            that is, `(n - i - 1)! = (n - (i + 1))!`
            """
            ans += cnt * factorial
            factorial *= n - i

        return ans
