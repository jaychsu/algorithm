class Solution:
    """
    @param: A: A list of integers
    @param: target: An integer
    @return: A list of lists of integers
    """
    def combinationSum(self, A, target):
        ans = []
        if not A:
            return ans

        A.sort()
        self.dfs(A, 0, target, ans, [])
        return ans

    def dfs(self, A, start, remaining, ans, path):
        if remaining == 0:
            ans.append(path[:])
            return

        for i in range(start, len(A)):
            if remaining < A[i]:
                # note that, its `return` here
                # since `remaining < A[i]` and `A[i] <= A[i + 1] <= ...`
                # so once it continued, all iteration after i is no need
                return

            path.append(A[i])
            self.dfs(A, i, remaining - A[i], ans, path)
            path.pop()
