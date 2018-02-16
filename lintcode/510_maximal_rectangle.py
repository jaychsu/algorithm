class Solution:
    def maximalRectangle(self, G):
        """
        :type G: List[List[str]]
        :rtype: int
        """
        ans = 0
        if not G or not G[0]:
            return ans

        m, n = len(G), len(G[0])
        L, R, H = {}, {}, {}

        for i in range(m):
            curr = 0  # left boundary
            for j in range(n):
                if G[i][j] == '1':
                    H[j] = H.get(j, 0) + 1
                    L[j] = max(L.get(j, 0), curr)
                else:
                    H[j] = L[j] = 0
                    curr = j + 1

            curr = n  # right boundary
            for j in range(n - 1, -1, -1):
                if G[i][j] == '1':
                    R[j] = min(R.get(j, n), curr)
                else:
                    R[j] = n
                    curr = j

                ans = max(
                    ans,
                    H[j] * (R[j] - L[j])
                )

        return ans


"""
Assuming matrix: [
  [1, 1, 0, 0, 1],
  [0, 1, 0, 0, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1]
]

Concept:
For each (i, j), 0 <= i < len(mat), 0 <= j < len(mat[0])
the rectangle area is (r[j] - l[j]) * h[j]

m = 0
v 1 1 0 0 1
h 1 1 0 0 1
l 0 0 0 0 4
r 2 2 5 5 5

m = 1
v 0 1 0 0 1
h 0 2 0 0 2
l 0 1 0 0 4
r 5 2 5 5 5

m = 2
v 0 0 1 1 1
h 0 0 1 1 3
l 0 0 2 2 4
r 5 5 5 5 5

m = 3
v 0 0 1 1 1
h 0 0 2 2 4
l 0 0 2 2 4
r 5 5 5 5 5

m = 4
v 0 0 0 0 1
h 0 0 0 0 5
l 0 0 0 0 4
r 5 5 5 5 5

max = 6 = (5 - 2) * 2
"""


# Mono Stack
# This problem could be treated as histogram, see lintcode#122
class Solution:
    def maximalRectangle(self, G):
        """
        :type G: List[List[str]]
        :rtype: int
        """
        ans = 0
        if not G or not G[0]:
            return ans

        m, n = len(G), len(G[0])
        H = [0] * n

        for i in range(m):
            for j in range(n):
                if G[i][j] == '1':
                    H[j] += 1
                else:
                    H[j] = 0

            ans = max(ans, self.largestRectangleArea(H))

            # To remove the trick `0`
            H.pop()

        return ans

    def largestRectangleArea(self, H):
        area = 0
        if not H:
            return area

        # To ensure the last element in monostack will be handled
        H.append(0)

        I = []
        left = height = 0

        for right in range(len(H)):
            while I and H[I[-1]] >= H[right]:
                height = H[I.pop()]
                left = I[-1] if I else -1
                area = max(
                    area,
                    height * (right - left - 1)
                )
            I.append(right)

        return area
