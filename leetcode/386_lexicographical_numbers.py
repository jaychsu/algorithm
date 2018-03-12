class Solution:
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans = []

        if not n:
            return ans

        stack = [1]

        while stack:
            x = stack.pop()
            ans.append(x)

            # considering the case no carry up if x + 1
            # that is, x in [1, 8]
            if x < n and x % 10 < 9:
                stack.append(x + 1)

            if x * 10 <= n:
                stack.append(x * 10)

        return ans
