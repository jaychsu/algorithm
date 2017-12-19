class Solution:
    def permute(self, A):
        """
        :type A: List[int]
        :rtype: List[List[int]]
        """
        if not A:
            return [[]]

        ans = []
        self.dfs(sorted(A), ans, [])
        return ans

    def dfs(self, A, ans, permutation):
        if len(permutation) >= len(A):
            ans.append(permutation)
            return

        for i in range(len(A)):
            if A[i] in permutation:
                continue

            self.dfs(A, ans, permutation + [A[i]])

            """
            backtracking is not allowed,
            since it will lead to got empty before exit
            """
