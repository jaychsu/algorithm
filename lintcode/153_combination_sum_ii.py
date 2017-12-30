class Solution:
    """
    @param: A: Given the candidate numbers
    @param: target: Given the target number
    @return: All the combinations that sum to target
    """
    def combinationSum2(self, A, target):
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
                return

            # to prevent [1', 2, 5] and [1", 2, 5]
            # appear in result at same time
            if i > start and A[i] == A[i - 1]:
                continue

            path.append(A[i])
            self.dfs(A, i + 1, remaining - A[i], ans, path)
            path.pop()
