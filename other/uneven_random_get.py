# TODO: do expectations like `chi-square calculator`
import random


def uneven_random_get(options, rate):
    """unevenly fetch the option according to the corresponding rate
    :type options: list[str]
    :type rate: list[num]
    :rtype: str

    >>> options = ['a', 'b', 'c']

    >>> ans = dict.fromkeys(options, 0)
    >>> for _ in range(10000):
    ...     c = uneven_random_get(options, [10, 10, 10])
    ...     ans[c] += 1
    >>> all(2000 <= ans[c] <= 4000 for c in options)
    True

    >>> ans = dict.fromkeys(options, 0)
    >>> for _ in range(10000):
    ...     c = uneven_random_get(options, [80, 10, 10])
    ...     ans[c] += 1
    >>> all((
    ...     7000 <= ans['a'] <= 9000,
    ...     0 <= ans['b'] <= 2000,
    ...     0 <= ans['c'] <= 2000,
    ... ))
    True
    """
    if not options or not rate or len(options) != len(rate):
        return ''

    num = 0
    rand = random.randint(1, sum(rate))

    for i in range(len(rate)):
        num += rate[i]

        if rand <= num:
            return options[i]
