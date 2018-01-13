class Solution:
    """
    @param: n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        ans = []
        if not n:
            return ans

        a = i3 = i5 = 1

        while a <= n:
            while a <= n and a < i3 * 3 and a < i5 * 5:
                ans.append(str(a))
                a += 1

            if a <= n and a == i3 * 3 and a == i5 * 5:
                ans.append('fizz buzz')
                a += 1
                i3 += 1
                i5 += 1
                continue

            while a <= n and a == i3 * 3:
                ans.append('fizz')
                a += 1
                i3 += 1

            while a <= n and a == i5 * 5:
                ans.append('buzz')
                a += 1
                i5 += 1

        return ans
