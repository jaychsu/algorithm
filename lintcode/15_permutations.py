class Solution:
    def permute(self, A):
        """
        :type A: List[int]
        :rtype: List[List[int]]
        """
        if not A:
            return [[]]

        ans = []
        A.sort()
        self.dfs(A, ans, [])
        return ans

    def dfs(self, A, ans, path):
        if not A:
            ans.append(path[:])
            return

        for i in range(len(A)):
            path.append(A[i])
            self.dfs(A[:i] + A[i + 1:], ans, path)
            path.pop()
