class Solution:
    def canTransform(self, start, end):
        """
        :type start: str
        :type end: str
        :rtype: bool
        """
        if len(start) != len(end):
            return False

        m, n = len(start), len(end)
        i = j = 0

        while i < m and j < n:
            while i < m and start[i] == 'X':
                i += 1
            while j < n and end[j] == 'X':
                j += 1

            if i == m and j == n:
                return True
            if i == m or j == n:
                return False

            if start[i] != end[j]:
                return False
            if start[i] == 'L' and j > i:
                return False
            if start[i] == 'R' and i > j:
                return False

            i += 1
            j += 1

        return True
