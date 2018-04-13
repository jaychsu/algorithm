class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if not secret or not guess or len(secret) != len(guess):
            return ''

        TMPL = '{}A{}B'
        bulls = 0
        cows = 0
        cnts = [0] * 10

        for i in range(len(secret)):
            s = ord(secret[i]) - ord('0')
            g = ord(guess[i]) - ord('0')

            if s == g:
                bulls += 1
                continue

            cnts[s] += 1
            cnts[g] -= 1

            if cnts[s] <= 0:
                cows += 1
            if cnts[g] >= 0:
                cows += 1

        return TMPL.format(bulls, cows)


class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        if not secret or not guess or len(secret) != len(guess):
            return ''

        TMPL = '{}A{}B'
        bulls = 0
        cows = 0
        cnt_s = [0] * 10
        cnt_g = [0] * 10

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                cnt_s[int(secret[i])] += 1
                cnt_g[int(guess[i])] += 1

        for i in range(10):
            cows += min(cnt_s[i], cnt_g[i])

        return TMPL.format(bulls, cows)
