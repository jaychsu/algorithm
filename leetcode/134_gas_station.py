class Solution(object):
    def canCompleteCircuit(self, G, C):
        """
        :type G: List[int]
        :type C: List[int]
        :rtype: int
        """
        NOT_FOUND = -1
        if not G or not C or len(G) != len(C):
            return NOT_FOUND

        end, start = 0, len(G) - 1
        _sum = G[start] - C[start]

        while start > end:
            if _sum >= 0:
                _sum += G[end] - C[end]
                end += 1
            else:
                start -= 1
                _sum += G[start] - C[start]

        return start if _sum >= 0 else NOT_FOUND
