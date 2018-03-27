"""
Definition of Interval.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


"""
Sweep Line
time: O(n)
space: O(n)
"""
class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: list[Interval]
        :rtype: bool
        """
        timeline = []

        for interval in intervals:
            timeline.append((interval.start, True))
            timeline.append((interval.end, False))

        timeline.sort()

        cnt = 0

        for time, is_start in timeline:
            if is_start:
                cnt += 1
            else:
                cnt -= 1

            if cnt > 1:
                return False

        return True


"""
Sorting
time: O(nlogn)
space: O(1)
"""
class Solution:
    def canAttendMeetings(self, intervals):
        """
        :type intervals: list[Interval]
        :rtype: bool
        """
        intervals.sort(key=lambda x: (x.start, x.end))

        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                return False

        return True
