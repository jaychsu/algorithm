class Solution:
    """
    @param: L: Given n pieces of wood with length L[i]
    @param: k: An integer
    @return: The maximum length of the small pieces
    """
    """
    Assuming the `m` is the maximum length
    len   | ... m-2 m-1 m m+1 m+2 ...
    check |  T   T   T  T  F   F   F
    * check: is it ok to cut into at least `k` pieces
    """
    def woodCut(self, L, k):
        if sum(L) < k:
            return 0

        l, m, r = 1, 1, max(L)
        pieces = 0
        while l + 1 < r:
            m = l + (r - l) // 2
            pieces = sum([h // m for h in L])
            if pieces < k:
                r = m
            else:
                l = m
        return r if sum([h // l for h in L]) < k else l
