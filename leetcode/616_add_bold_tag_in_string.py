"""
>>> gotcha = []
>>> for s in (Solution(),):
...     for _in, _out in (
...         (('', ['']), ''),
...         (('abcxyz123', ['abc', '123']), '<b>abc</b>xyz<b>123</b>'),
...         (('aaabbcc', ['aaa','aab','bc']), '<b>aaabbc</b>c'),
...         (('aabcd', ['ab', 'bc']), 'a<b>abc</b>d'),
...     ):
...         res = s.addBoldTag(*_in)
...         if res != _out: print(_in, res)
...         gotcha.append(res == _out)
>>> bool(gotcha) and all(gotcha)
True
"""


class Solution:
    def addBoldTag(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: str
        """
        if not s or not words:
            return ''

        TMPL = '<b>{}</b>'
        n = len(s)
        ans = []
        is_bold = [False] * n
        left = right = 0

        for left in range(n):
            for w in words:
                size = len(w)

                if s[left:left + size] == w and left + size > right:
                    right = left + size

            is_bold[left] = right > left

        left = right = 0

        while left < n:
            if not is_bold[left]:
                ans.append(s[left])
                left += 1
                continue

            right = left

            while right < n and is_bold[right]:
                right += 1

            ans.append(TMPL.format(s[left:right]))
            left = right  # imply left' = left + 1

        return ''.join(ans)
