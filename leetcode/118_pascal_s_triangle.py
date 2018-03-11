class Solution:
    def generate(self, num_rows):
        """
        :type num_rows: int
        :rtype: List[List[int]]
        """
        ans = []
        if not num_rows:
            return ans

        ans.append([1])

        for i in range(1, num_rows):
            path = [ans[i - 1][0]]

            for j in range(1, len(ans[i - 1])):
                path.append(ans[i - 1][j] + ans[i - 1][j - 1])

            path.append(ans[i - 1][-1])
            ans.append(path)

        return ans


class Solution:
    def generate(self, num_rows):
        """
        :type num_rows: int
        :rtype: List[List[int]]
        """
        ans = []
        if not num_rows:
            return ans

        ans.append([1])

        for i in range(1, num_rows):
            ans.append([
                (ans[i - 1] + [0])[j] + ([0] + ans[i - 1])[j]
                for j in range(len(ans[i - 1]) + 1)
            ])

        return ans
