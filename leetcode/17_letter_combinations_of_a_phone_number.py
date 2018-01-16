class Solution:
    def letterCombinations(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        ans = []
        if not s:
            return ans
        for c in s:
            if c == '0' or c == '1':
                return ans

        C = {
            '2': 'abc', '3': 'def',  '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
        }

        ans.extend(list(C[s[0]]))
        for i in range(1, len(s)):
            _queue = []
            for char in ans:
                for _char in C[s[i]]:
                    _queue.append(char + _char)
            ans = _queue

        return ans
