"""
TODO:
1. do expectations like `chi-square calculator`
"""
import random


def uneven_random_get(options, rate):
    """unevenly fetch the option according to the corresponding rate
    :type options: list[str]
    :type rate: list[num]
    :rtype: str
    """
    if not options or not rate or len(options) != len(rate):
        return ''

    num = 0
    rand = random.randint(1, sum(rate))

    for i in range(len(rate)):
        num += rate[i]

        if num >= rand:
            return options[i]

    return options[0]


def uneven_random_get2(options, rate):
    """unevenly fetch the option according to the corresponding rate
    :type options: list[str]
    :type rate: list[num]
    :rtype: str
    """
    if not options or not rate or len(options) != len(rate):
        return ''

    k = total = 0

    for i in range(len(rate)):
        if random.randrange(total + rate[i]) >= total:
            k = i

        total += rate[i]

    return options[k]


if __name__ == '__main__':
    gotcha = []
    options = 'abc'

    for uneven_get in (uneven_random_get, uneven_random_get2):
        freq = dict.fromkeys(options, 0)
        for _ in range(10000):
            c = uneven_get(options, (10, 10, 10))
            freq[c] += 1
        gotcha.append(all(2833 <= freq[c] <= 3833 for c in options))

        freq = dict.fromkeys(options, 0)
        for _ in range(10000):
            c = uneven_get(options, (1, 1, 1))
            freq[c] += 1
        gotcha.append(all(2833 <= freq[c] <= 3833 for c in options))

        freq = dict.fromkeys(options, 0)
        for _ in range(10000):
            c = uneven_get(options, (8, 1, 1))
            freq[c] += 1
        gotcha.append(all((
            7500 <= freq['a'] <= 8500,
            500 <= freq['b'] <= 1500,
            500 <= freq['c'] <= 1500,
        )))

    print(bool(gotcha) and all(gotcha))
