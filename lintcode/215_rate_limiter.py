class Solution:
    time_in_sec = {
        's': 1,
        'm': 60,
        'h': 3600,
        'd': 86400,
    }

    logs = {}

    """
    @param: timestamp: the current timestamp
    @param: event: the string to distinct different event
    @param: rate: the format is [integer]/[s/m/h/d]
    @param: increment: whether we should increase the counter
    @return: true or false to indicate the event is limited or not
    """
    def isRatelimited(self, timestamp, event, rate, increment):
        ltd_times, time_range = rate.split('/')
        ltd_times = int(ltd_times)
        last_valid_time = timestamp - self.time_in_sec.get(time_range, 1) + 1

        if event not in self.logs:
            self.logs[event] = []

        valid_logs = self.find_valid_logs(self.logs[event], last_valid_time)
        is_ltd = valid_logs >= ltd_times
        if increment and not is_ltd:
            self.logs[event].append(timestamp)

        return is_ltd

    def find_valid_logs(self, logs, last_valid_time):
        if not logs or logs[-1] < last_valid_time:
            return 0

        left, mid, right = 0, 0, len(logs) - 1
        while left + 1 < right:
            mid = left + (right - left) // 2
            if logs[mid] < last_valid_time:
                left = mid
            else:
                right = mid

        start = right if logs[left] < last_valid_time else left
        return len(logs) - 1 - start + 1
