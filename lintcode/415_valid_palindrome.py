"""
Test Case:

"ab"
: `while left + 1 < right:` -> `while left < right:`
"""


class Solution:
    """
    @param: s: A string
    @return: Whether the string is a valid palindrome
    """
    def isPalindrome(self, s):
        if not s:
            return True

        n = len(s)
        left, right = 0, n - 1

        while left < right:
            while left < n and not self.is_valid(s[left]):
                left += 1

            # '' or ', .,;'
            if left == n:
                return True

            while right >= 0 and not self.is_valid(s[right]):
                right -= 1

            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True

    def is_valid(self, s):
        s = s.lower()
        return (ord('a') <= ord(s) <= ord('z') or
                ord('0') <= ord(s) <= ord('9'))
