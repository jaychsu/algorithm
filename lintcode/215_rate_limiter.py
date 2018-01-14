class Solution:
    def __init__(self):
        self.T = {
            's': 1,
            'm': 60,
            'h': 3600,
            'd': 86400,
        }
        self.logs = {}

    """
    @param: timestamp: the current timestamp
    @param: event: the string to distinct different event
    @param: rate: the format is [integer]/[s/m/h/d]
    @param: increment: whether we should increase the counter
    @return: true or false to indicate the event is limited or not
    """
    def isRatelimited(self, timestamp, event, rate, increment):
        freq, level = rate.split('/')
        freq = int(freq)
        last_valid = timestamp - self.T.get(level, 1) + 1

        if event not in self.logs:
            self.logs[event] = []

        is_limited = self.check_limited(self.logs[event], last_valid, freq)
        if increment and not is_limited:
            self.logs[event].append(timestamp)

        return is_limited

    def check_limited(self, logs, last_valid, freq):
        """
        if no logs here and freq is 0
        => is limited
        """
        if not logs or logs[-1] < last_valid:
            return freq == 0

        left, right = 0, len(logs) - 1
        while left + 1 < right:
            mid = (left + right) // 2
            if logs[mid] < last_valid:
                left = mid
            else:
                right = mid

        if logs[left] < last_valid:
            left = right

        return len(logs) - left >= freq
