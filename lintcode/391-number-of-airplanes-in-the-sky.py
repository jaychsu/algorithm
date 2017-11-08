"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param: airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """
    def countOfAirplanes(self, airplanes):
        ans = 0
        if not airplanes:
            return ans
        cnt = 0
        timeline = []
        for interval in airplanes:
            timeline.append((interval.start, 1))
            timeline.append((interval.end, 0))
        timeline.sort()
        for _, in_sky in timeline:
            if in_sky:
                cnt += 1
            else:
                cnt -= 1
            ans = max(ans, cnt)
        return ans
