import collections


class Solution:
    """
    maintain a list to record the timestamps for every event
    and if a query coming => we need ensure
    there is no more `freq` logs between `begin_time` and `timestamp`(current)

    1. split rate
    2. cal begin time
    3. do binary searching to find the closest index of `begin time`
    4. count the child between res of (3) to the end of list
    5. if cnt >= freq => is limited
    """
    def __init__(self):
        self.times = {
            's': 1,
            'm': 60,
            'h': 3600,
            'd': 86400,
        }
        self.logs = collections.defaultdict(list)

    def isRatelimited(self, timestamp, event, rate, increment):
        """
        :type timestamp: int
        :type event: str
        :type rate: str
        :type increment: bool
        :rtype: bool
        """
        if '/' not in rate:
            return False

        freq, t = rate.split('/')
        freq = int(freq)
        begin_time = timestamp - self.times.get(t, 1) + 1
        is_limited = self.check_limited(event, freq, begin_time)

        if increment and not is_limited:
            self.logs[event].append(timestamp)

        return is_limited

    def check_limited(self, event, freq, begin_time):
        logs = self.logs[event]

        if not logs or logs[-1] < begin_time:
            # if freq is 0 => is limited
            return freq == 0

        left, right = 0, len(logs) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if logs[mid] < begin_time:
                left = mid
            else:
                right = mid

        mid = left if logs[left] >= begin_time else right
        return len(logs) - mid >= freq
