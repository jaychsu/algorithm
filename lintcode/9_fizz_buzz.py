class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []

        if not n:
            return ans

        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                ans.append('FizzBuzz')
            elif i % 3 == 0:
                ans.append('Fizz')
            elif i % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(i))

        return ans


class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
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
