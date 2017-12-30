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
        A.sort()
        self.dfs(A, ans, [])
        return ans

    def dfs(self, A, ans, path):
        if not A:
            ans.append(path[:])
            return

        for i in range(len(A)):
            """
            ignore same num
            """
            if i > 0 and A[i] == A[i - 1]:
                continue

            """
            ignore self
            """
            path.append(A[i])
            self.dfs(A[:i] + A[i + 1:], ans, path)
            path.pop()


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
        A.sort()
        self.dfs(A, visited, ans, [])
        return ans

    def dfs(self, A, visited, ans, path):
        if len(path) == len(A):
            ans.append(path[:])
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
            if i > 0 and not visited[i - 1] and A[i] == A[i - 1]:
                continue

            visited[i] = True
            path.append(A[i])
            self.dfs(A, visited, ans, path)
            visited[i] = False
            path.pop()
