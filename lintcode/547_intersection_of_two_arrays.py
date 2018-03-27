class Solution:
    def intersection(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: List[int]
        """
        ans = []

        if not a or not b:
            return ans

        s = set(a)
        t = set(b)

        for x in s:
            if x in t:
                ans.append(x)

        return ans


class Solution:
    def intersection(self, a, b):
        """
        :type a: List[int]
        :type b: List[int]
        :rtype: List[int]
        """
        ans = []

        if not a or not b:
            return ans

        a.sort()
        b.sort()

        m, n = len(a), len(b)
        i = j = 0

        while i < m and j < n:
            if a[i] == b[j]:
                if not ans or a[i] != ans[-1]:
                    ans.append(a[i])
                i += 1
                j += 1
            elif a[i] < b[j]:
                i += 1
            else:
                j += 1

        return ans
