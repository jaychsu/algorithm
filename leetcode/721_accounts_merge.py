class Solution:
    def accountsMerge(self, A):
        """
        :type A: List[List[str]]
        :rtype: List[List[str]]
        """
        if not A:
            return []

        M = {}  # mails
        M2N = {}  # mail to name
        for L in A:
            for i in range(1, len(L)):
                M2N[L[i]] = L[0]
                self.connect(M, L[i], L[1])

        for a in M:
            self.find(M, a)

        res = {}
        for m1, m0 in M.items():
            if m0 not in res:
                res[m0] = []

            res[m0].append(m1)

        return [[M2N[m]] + sorted(M) for m, M in res.items()]

    def connect(self, N, a, b):
        _a = self.find(N, a)
        _b = self.find(N, b)

        if _a is not _b:
            N[_a] = _b

    def find(self, N, a):
        if a not in N:
            N[a] = a
            return a
        if N[a] is a:
            return a

        N[a] = self.find(N, N[a])
        return N[a]
