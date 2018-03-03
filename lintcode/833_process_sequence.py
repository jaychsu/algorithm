class Solution:
    """
    @param logs: Sequence of processes
    @param queries: Sequence of queries
    @return: Return the number of processes
    """
    def numberOfProcesses(self, logs, queries):
        time = []

        # 0: end, 1: start, 2: in progress
        for log in logs:
            time.append((log.start, 1))
            time.append((log.end + 1, 0))

        for t in queries:
            time.append((t, 2))

        time.sort()

        cnt = 0
        time2cnt = {}

        for t, status in time:
            if status == 0:
                cnt -= 1
            elif status == 1:
                cnt += 1

            time2cnt[t] = cnt

        return [time2cnt[t] for t in queries]
