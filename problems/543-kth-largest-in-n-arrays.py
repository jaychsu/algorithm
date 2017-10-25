import heapq

class Solution:

    """
    @param: arrays: a list of array
    @param: k: An integer
    @return: an integer, K-th largest element in N arrays
    """
    def KthInArrays(self, arrays, k):
        res = []
        for arr in arrays: res += arr
        if k > len(res):
            return 'error'
        res.sort()
        return res[-k]
