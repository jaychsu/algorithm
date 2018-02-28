class Solution:
    def countAndSay(self, N):
        """
        :type N: int
        :rtype: str
        """
        queue = '1'

        if not N:
            return queue

        _queue = []

        for _ in range(N - 1):
            cnt = 0
            char = queue[0]

            for c in queue:
                if c == char:
                    cnt += 1
                    continue
                _queue.extend((str(cnt), char))
                cnt = 1
                char = c

            _queue.extend((str(cnt), char))
            queue, _queue = ''.join(_queue), []

        return queue
