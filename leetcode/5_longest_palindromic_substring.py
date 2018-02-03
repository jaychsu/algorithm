class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ''

        start = size = 0

        for i in range(len(s)):
            _start, _size = self.check_palindrome(s, i, i)

            if _size > size:
                size = _size
                start = _start

            _start, _size = self.check_palindrome(s, i, i + 1)

            if _size > size:
                size = _size
                start = _start

        return s[start:start + size]

    def check_palindrome(self, s, left, right):
        n = len(s)

        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1

        return left + 1, right - left - 1
