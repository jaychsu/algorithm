class Solution:
    def minArea(self, image, x, y):
        """
        :type image: list[str]
        :type x: int
        :type y: int
        :rtype: int
        """
        if not image or not image[0]:
            return 0

        m, n = len(image), len(image[0])

        top = self.binary_search(image, 0, x, self.is_empty_row)
        bottom = self.binary_search(image, m - 1, x, self.is_empty_row)
        left = self.binary_search(image, 0, y, self.is_empty_col)
        right = self.binary_search(image, n - 1, y, self.is_empty_col)

        return (bottom - top + 1) * (right - left + 1)

    def binary_search(self, image, start, end, is_empty):
        check = None

        if start < end:
            check = lambda start, end: start + 1 < end
        else:
            check = lambda start, end: start - 1 > end

        while check(start, end):
            mid = (start + end) // 2

            if is_empty(image, mid):
                start = mid
            else:
                end = mid

        return end if is_empty(image, start) else start

    def is_empty_row(self, image, x):
        for col in image[x]:
            if col == '1':
                return False
        return True

    def is_empty_col(self, image, y):
        for row in image:
            if row[y] == '1':
                return False
        return True
