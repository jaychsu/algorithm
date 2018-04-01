"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: list[Interval]
        :rtype: int
        """
        ans = 0

        if not intervals:
            return ans

        time = []

        for x in intervals:
            time.append((x.start, True))
            time.append((x.end, False))

        time.sort()

        cnt = 0

        for t, is_start in time:
            if is_start:
                cnt += 1
            else:
                cnt -= 1

            if cnt > ans:
                ans = cnt

        return ans
