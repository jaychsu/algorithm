"""
Test Case:

[3,3,0,3]
"""


"""
dfs with ignoring self and same num
"""
class Solution:
    def permuteUnique(self, A):
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
        if not A:
            ans.append(permutation)
            return

        for i in range(len(A)):
            """
            ignore same num
            """
            if i > 0 and A[i - 1] == A[i]:
                continue

            """
            ignore self
            """
            self.dfs(A[:i] + A[i + 1:], ans, permutation + [A[i]])


"""
dfs with visited indices
"""
class Solution:
    def permuteUnique(self, A):
        """
        :type A: List[int]
        :rtype: List[List[int]]
        """

        if not A:
            return [[]]

        ans = []
        visited = [False] * len(A)
        self.dfs(sorted(A), ans, [], visited)
        return ans

    def dfs(self, A, ans, permutation, visited):
        if len(permutation) >= len(A):
            ans.append(permutation)
            return

        for i in range(len(A)):
            if visited[i]:
                continue

            """
            example: [0, 3, 3', 3"]
            if current iteration is `3"`
            we need to ensure `3`, `3'` is picked
            otherwise repeated result will be included
            """
            if (i > 0 and A[i - 1] == A[i] and
                not visited[i - 1]):
                continue

            visited[i] = True
            self.dfs(A, ans, permutation + [A[i]], visited)
            visited[i] = False
