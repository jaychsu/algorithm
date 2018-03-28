"""
This problem should be discussed, and there might be 3 ways to solve
REF: http://www.1point3acres.com/bbs/thread-218909-1-1.html

1. add specific char to separate. '@'
2. encode number anyway
3. cheating, like '1aaaaa' -> '1a4xa'


>>> CASE = (
...     ('ff', 'ff'),
...     ('fff', 'fff'),
...     ('ffff', '4xf'),
...     ('1xt', '1x1xt'),
...     ('5xt', '1x5xt'),
...     ('1aaaaa', '1x15xa'),
...     ('3aaaaa', '1x35xa'),
...     ('123aaaa', '1x11x21x34xa'),
...     ('aaabbbbcccc', 'aaa4xb4xc'),
... )

>>> all(decode(encode(inpt)) == inpt for inpt, _ in CASE)
True
>>> all(encode(inpt) == oupt for inpt, oupt in CASE)
True
>>> all(decode(oupt) == inpt for inpt, oupt in CASE)
True
"""


def encode(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return ''

    res = []
    cnt = 1
    char = s[0]

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            cnt += 1
            continue

        # s[i] != s[i - 1]
        if char.isdigit() or cnt > 3:
            res.append(str(cnt))
            res.append('x')
            res.append(char)
        else:
            res.append(char * cnt)

        cnt = 1
        char = s[i]

    if char.isdigit() or cnt > 3:
        res.append(str(cnt))
        res.append('x')
        res.append(char)
    else:
        res.append(char * cnt)

    return ''.join(res)


def decode(s):
    """
    :type s: str
    :rtype: str
    """
    if not s:
        return ''

    res = []
    i = 0
    n = len(s)

    while i < n:
        is_digit = s[i].isdigit()

        if is_digit and i + 2 >= n:
            return ''

        if is_digit:
            res.append(int(s[i]) * s[i + 2])
            i += 3
        else:
            res.append(s[i])
            i += 1

    return ''.join(res)
