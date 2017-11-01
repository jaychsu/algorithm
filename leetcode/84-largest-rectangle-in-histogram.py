"""
Test Case:
[2,1,5,6,2,3]
[1,1]
"""
class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        ans = 0
        if not heights or len(heights) < 1:
            return ans

        # To ensure the last element in monostack will be handled
        heights.append(0)

        indices = []
        top = l = h = 0

        # https://goo.gl/nLfT99
        for r in range(len(heights)):
            while indices and heights[indices[-1]] >= heights[r]:
                top = indices.pop()
                h = heights[top]
                l = indices[-1] if indices else -1
                ans = max(ans, h * (r - l - 1))
            indices.append(r)
        return ans
