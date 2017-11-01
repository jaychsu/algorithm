"""
Test Case:
[2,1,5,6,2,3]
[1,1]
"""
class Solution:
    """
    @param: height: A list of integer
    @return: The area of largest rectangle in the histogram
    """
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
