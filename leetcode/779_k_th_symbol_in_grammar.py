class Solution:
    def kthGrammar(self, N, K):
        """
        :type N: int
        :type K: int
        :rtype: int
        """
        if N == 1:
            return 0

        if K % 2 == 0:
            if self.kthGrammar(N - 1, K // 2) == 0:
                return 1
            else:
                return 0
        else:
            if self.kthGrammar(N - 1, (K + 1) // 2) == 0:
                return 0
            else:
                return 1
