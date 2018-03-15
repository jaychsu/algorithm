import collections


class Solution:
    def isRectangleCover(self, recs):
        """
        :type recs: List[List[int]]
        :rtype: bool
        """
        if not recs:
            return False

        left = bottom = float('inf')
        right = top = float('-inf')
        points = collections.defaultdict(int)

        for l, b, r, t in recs:
            left = min(left, l)
            bottom = min(bottom, b)
            right = max(right, r)
            top = max(top, t)

            for x, y, val in (
                (l, b, 1),
                (r, b, 2),
                (r, t, 4),
                (l, t, 8),
            ):
                if points[x, y] & val:
                    return False
                points[x, y] |= val

        if any(
            # only check the mid-points
            val not in (3, 6, 9, 12, 15)
            for (x, y), val in points.items()
            if left < x < right or bottom < y < top
        ):
            return False

        return True
