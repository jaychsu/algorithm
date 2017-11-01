class Solution:
    """
    @param: matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        ans = 0
        if not matrix or len(matrix) < 1:
            return ans
        m, n = len(matrix), len(matrix[0])
        l, r, h = {}, {}, {}
        curr = 0
        for i in range(m):

            curr = 0
            for j in range(n):
                if int(matrix[i][j]) > 0:
                    h[j] = h.get(j, 0) + 1
                    l[j] = max(l.get(j, 0), curr)
                else:
                    h[j] = l[j] = 0
                    curr = j + 1

            curr = n
            for j in range(n - 1, -1, -1):
                if int(matrix[i][j]) > 0:
                    r[j] = min(r.get(j, n), curr)
                else:
                    r[j] = n
                    curr = j
                ans = max(ans, (r[j] - l[j]) * h[j])

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
    """
    @param: matrix: a boolean 2D matrix
    @return: an integer
    """
    def maximalRectangle(self, matrix):
        ans = 0
        if not matrix or len(matrix) < 1:
            return ans
        height = [0] * len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if int(matrix[i][j]) == 0:
                    height[j] = 0
                else:
                    height[j] += 1
            ans = max(ans, self.largestRectangleArea(height))

            # To remove the trick `0`
            height.pop()

        return ans

    def largestRectangleArea(self, height):
        ans = 0
        if not height or len(height) < 1:
            return ans

        # To ensure the last element in monostack will be handled
        height.append(0)

        indices = []
        top = l = h = 0

        # https://goo.gl/nLfT99
        for r in range(len(height)):
            while indices and height[indices[-1]] >= height[r]:
                top = indices.pop()
                h = height[top]
                l = indices[-1] if indices else -1
                ans = max(ans, h * (r - l - 1))
            indices.append(r)
        return ans
