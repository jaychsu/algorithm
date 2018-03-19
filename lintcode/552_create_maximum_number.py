class Solution:
    def maxNumber(self, a, b, k):
        """
        :type a: list[int]
        :type b: list[int]
        :type k: int, k <= m + n
        :rtype: list[int]
        """
        ans = []

        for size in range(
            max(0, k - len(a)),
            min(k, len(b)) + 1
        ):
            res = self.merge(
                self.get_max(a, k - size),
                self.get_max(b, size)
            )
            ans = max(ans, res)

        return ans

    def get_max(self, a, size):
        res = []
        n = len(a)

        for i in range(n):
            while (
                res and
                len(res) + n - i > size and
                res[-1] < a[i]
            ):
                res.pop()

            if len(res) < size:
                res.append(a[i])

        return res

    def merge(self, a, b):
        return [
            max(a, b).pop(0)
            for _ in range(len(a) + len(b))
        ]
