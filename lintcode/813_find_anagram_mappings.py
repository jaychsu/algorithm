"""
Find last pos
"""
class Solution:
    def anagramMappings(self, a, b):
        """
        :type a: list[int]
        :type b: list[int]
        :rtype: list[int]
        """
        if not a or not b or len(a) != len(b):
            return []

        n = len(a)
        ans = [-1] * n
        b2i = {}

        for i in range(n):
            b2i[b[i]] = i

        for i in range(n):
            if a[i] not in b2i:
                return []

            ans[i] = b2i[a[i]]

        return ans


"""
Strict
"""
class Solution:
    def anagramMappings(self, a, b):
        """
        :type a: list[int]
        :type b: list[int]
        :rtype: list[int]
        """
        if not a or not b or len(a) != len(b):
            return []

        n = len(a)
        ans = [-1] * n
        b2i = {}

        for i in range(n):
            if b[i] not in b2i:
                b2i[b[i]] = []

            b2i[b[i]].append(i)

        for i in range(n):
            if not b2i.get(a[i]):
                # a[i] not in b2i
                # b2i[a[i]] is empty list
                return []

            ans[i] = b2i[a[i]].pop()

        return ans
