class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: list[str]
        """
        if not n:
            return ['']

        ans = None

        if n & 1:
            ans = ['0', '1', '8']
            n -= 1
        else:
            ans = ['']

        while n > 0:
            _queue = []

            for s in ans:
                if n != 2:  # last loop
                    _queue.append('0' + s + '0')

                _queue.append('1' + s + '1')
                _queue.append('8' + s + '8')
                _queue.append('6' + s + '9')
                _queue.append('9' + s + '6')

            ans = _queue
            n -= 2

        return ans
