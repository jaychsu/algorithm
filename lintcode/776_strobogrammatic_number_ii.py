class Solution:
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: list[str]
        """
        ans = ['']

        if not n:
            return ans

        if n & 1:
            ans = ['0', '1', '8']
            n -= 1

        while n:
            queue = []

            for s in ans:
                if n != 2:
                    queue.append('0' + s + '0')

                queue.append('1' + s + '1')
                queue.append('8' + s + '8')
                queue.append('6' + s + '9')
                queue.append('9' + s + '6')

            ans = queue
            n -= 2

        return ans
