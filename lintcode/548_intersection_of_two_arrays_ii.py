class Solution:
    def intersect(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        ans = []
        if not A or not B:
            return ans

        F = {}
        for a in B:
            F[a] = F.get(a, 0) + 1

        for a in A:
            if not F.get(a):
                continue
            ans.append(a)
            F[a] -= 1

        return ans


class Solution:
    """
    @param: A: an integer array
    @param: B: an integer array
    @return: an integer array
    """
    def intersection(self, A, B):
        ans = []
        if not A or not B:
            return ans

        A.sort()
        B.sort()

        i = j = 0
        while i < len(A) and j < len(B):
            if A[i] == B[j]:
                ans.append(A[i])
                i += 1
                j += 1
                continue
            if A[i] < B[j]:
                i += 1
            else:
                j += 1

        return ans
