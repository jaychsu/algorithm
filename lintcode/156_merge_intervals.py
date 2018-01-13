class Solution:
    """
    @param: A: interval list.
    @return: A new interval list.
    """
    def merge(self, A):
        ans = []
        if not A:
            return ans

        A.sort(key=lambda I: (I.start, I.end))

        for I in A:
            if not ans or ans[-1].end < I.start:
                ans.append(I)
                continue

            if I.end > ans[-1].end:
                ans[-1].end = I.end

        return ans
