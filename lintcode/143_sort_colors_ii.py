"""
Rainbow Sort
time: O(nlogk)
"""
class Solution:
    """
    @param: colors: A list of integer
    @param: k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        if not colors or not k:
            return
        self.rainbow_sort(colors, 0, len(colors) - 1, 1, k)

    def rainbow_sort(self, colors, start, end, color_from, color_to):
        """
        like quick sort
        """
        if color_from >= color_to:
            return
        if start >= end:
            return

        left, right = start, end
        color_mid = (color_from + color_to) // 2
        while left <= right:
            while left <= right and colors[left] <= color_mid:
                left += 1
            while left <= right and colors[right] > color_mid:
                right -= 1
            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.rainbow_sort(colors, start, right, color_from, color_mid)
        self.rainbow_sort(colors, left, end, color_mid + 1, color_to)


"""
TLE
Extend from sort color
time: O(nk)
"""
class Solution:
    """
    @param: colors: A list of integer
    @param: k: An integer
    @return: nothing
    """
    def sortColors2(self, colors, k):
        """
        1. ensure the `min_color` in the `left_scope`,
           and the `max_color` in the `right_scope`
           in every iteration
        2. keep sorting the `mid_scope` to
           pick min/max color to the left/right scope
        """
        count = 0
        n = len(colors)
        left, right = 0, n - 1
        i = _min = _max = 0

        while count < k:
            _min = _max = colors[left]
            for i in range(left + 1, right + 1):
                if colors[i] < _min:
                    _min = colors[i]
                if colors[i] > _max:
                    _max = colors[i]

            i = left
            while i <= right:
                if colors[i] == _min:
                    colors[left], colors[i] = colors[i], colors[left]
                    left += 1
                    i += 1
                elif _min < colors[i] < _max:
                    # leave it to
                    # the next iteration of `while count < k` to sort
                    i += 1
                else:
                    colors[i], colors[right] = colors[right], colors[i]
                    right -= 1

            count += 2
