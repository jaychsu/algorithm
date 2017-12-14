from heapq import heappop, heappush


class Solution:
    """
    @param: k: An integer
    """
    def __init__(self, k):
        self.k = k
        self.top_k = []

    """
    @param: num: Number to be added
    @return: nothing
    """
    def add(self, num):
        heappush(self.top_k, num)

        if len(self.top_k) > self.k:
            heappop(self.top_k)

    """
    @return: Top k element
    """
    def topk(self):
        return sorted(self.top_k, reverse=True)
