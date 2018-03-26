# TODO: do expectations like `chi-square calculator`
import random


class Solution:
    def uneven_random_get(self, options, rate):
        """unevenly fetch the option according to the corresponding rate
        :type options: list[str]
        :type rate: list[num]
        :rtype: str

        >>> s = Solution()
        >>> options = ['a', 'b', 'c']

        >>> ans = dict.fromkeys(options, 0)
        >>> for _ in range(10000):
        ...     c = s.uneven_random_get(options, [33, 33, 34])
        ...     ans[c] += 1
        >>> [2000 <= ans[c] <= 4000 for c in options]
        [True, True, True]

        >>> ans = dict.fromkeys(options, 0)
        >>> for _ in range(10000):
        ...     c = s.uneven_random_get(options, [90, 10, 10])
        ...     ans[c] += 1
        >>> [8000 <= ans['a'] <= 10000, 0 <= ans['b'] <= 2000, 0 <= ans['c'] <= 2000]
        [True, True, True]
        """
        if not options or not rate or len(options) != len(rate):
            return ''

        num = 0
        rand = random.randint(1, sum(rate))

        for i in range(len(rate)):
            num += rate[i]

            if rand <= num:
                return options[i]
