class Solution:
    def topKFrequent(self, A, k):
        """
        :type A: List[int]
        :type k: int
        :rtype: List[int]
        """
        ans = []
        if not A:
            return ans

        F = {}
        for a in A:
            F[a] = F.get(a, 0) + 1

        for a, _ in sorted(F.items(), key=lambda x: -x[1]):
            if k == 0:
                break

            ans.append(a)
            k -= 1

        return ans
