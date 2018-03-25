"""
REF: https://leetcode.com/problems/palindrome-pairs/discuss/79199/150-ms-45-lines-JAVA-solution

Main Concept:

1. The <= in for (int j=0; j<=words[i].length(); j++) is aimed to handle empty string in the input. Consider the test case of [“a”, “”];
2. Since we now use <= in for (int j=0; j<=words[i].length(); j++) instead of <. There may be duplicates in the output (consider test case [“abcd”, “dcba”]). Therefore I put a str2.length()!=0 to avoid duplicates.
"""
class Solution:
    def palindromePairs(self, words):
        """
        :type words: list[str]
        :rtype: list[list[int]]
        """
        ans = []

        if not words:
            return ans

        n = len(words)
        w2i = {}

        for i in range(n):
            w2i[words[i]] = i

        for i in range(n):
            for j in range(len(words[i]) + 1):
                s = words[i][:j]
                t = words[i][j:]
                _s = ''.join(reversed(s))
                _t = ''.join(reversed(t))

                if (self.is_palindrome(s) and
                    _t in w2i and
                    w2i[_t] != i
                ):
                    ans.append([w2i[_t], i])

                if (self.is_palindrome(t) and
                    len(t) != 0 and  # since len(word) + 1, may empty here
                    _s in w2i and
                    w2i[_s] != i
                ):
                    ans.append([i, w2i[_s]])

        return ans

    def is_palindrome(self, word):
        n = len(word)
        left, right = 0, n - 1

        while left < right:
            if word[left] != word[right]:
                return False

            left += 1
            right -= 1

        return True


"""
TLE: Brute Force
"""
class Solution:
    def palindromePairs(self, words):
        """
        :type words: list[str]
        :rtype: list[list[int]]
        """
        ans = []

        if not words:
            return ans

        n = len(words)

        for i in range(n):
            for j in range(i):
                if self.is_palindrome(words, i, j):
                    ans.append([i, j])

                if self.is_palindrome(words, j, i):
                    ans.append([j, i])

        return ans

    def is_palindrome(self, words, i, j):
        s, t = words[i], words[j]
        a, b = len(s), len(t)
        n = a + b
        left, right = 0, n - 1

        while left < right:
            if left >= a and t[left - a] != t[right - a]:
                return False
            elif right < a and s[left] != s[right]:
                return False
            elif left < a and right >= a and s[left] != t[right - a]:
                return False

            left += 1
            right -= 1

        return True


"""
TLE: Brute Force
"""
class Solution:
    def palindromePairs(self, words):
        """
        :type words: list[str]
        :rtype: list[list[int]]
        """
        ans = []

        if not words:
            return ans

        n = len(words)

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue

                if self.is_palindrome(words[i] + words[j]):
                    ans.append([i, j])

        return ans

    def is_palindrome(self, s):
        n = len(s)
        left, right = 0, n - 1

        while left < right:
            if s[left] != s[right]:
                return False

            left += 1
            right -= 1

        return True
