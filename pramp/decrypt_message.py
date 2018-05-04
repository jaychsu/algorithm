"""
Encryption Rules:
1. add 1 to the ascii of first letter
2. add the ascii of prev letter, form second to last
3. keep substract 26 from every letter until it is in [ord('a'), ord('z')]

Testing:
>>> gotcha = []
>>> for origin, encryption in (
...     ('crime', 'dnotq'),
...     ('encyclopedia', 'flgxswdliefy'),
...     ('qqqqq', 'rajsb'),
...     ('abcdefghijklmnopqrstuvwxyz', 'bvqmjhgghjmqvbiqzjugthwmdv'),
...     ('drugtrafficking', 'eobamwpnlmhklrq'),
...     ('', ''),
... ):
...     res = encrypt(origin)
...     if res != encryption: print('L18', origin, res)
...     gotcha.append(res == encryption)
...
...     res = decrypt(encryption)
...     if res != origin: print('L22', encryption, res)
...     gotcha.append(res == origin)
...
...     res = decrypt(encrypt(origin))
...     if res != origin: print('L26', origin, res)
...     gotcha.append(res == origin)
...
...     res = decrypt2(encryption)
...     if res != origin: print('L30', encryption, res)
...     gotcha.append(res == origin)
...
...     res = decrypt2(encrypt(origin))
...     if res != origin: print('L34', origin, res)
...     gotcha.append(res == origin)
>>> bool(gotcha) and all(gotcha)
True
"""


def encrypt(word):
    if not word:
        return ''

    a = ord('a')
    ans = [ord(c) for c in word]
    cumul = 1

    for i in range(len(word)):
        cumul += ans[i]
        ans[i] = chr((cumul - a) % 26 + a)

    return ''.join(ans)


def decrypt(word):
    if not word:
        return ''

    a = ord('a')
    ans = [ord(c) for c in word]

    for i in range(len(word) - 1, -1, -1):
        if i == 0:
            ans[i] = chr((ans[i] - 1 - a) % 26 + a)
        else:
            ans[i] = chr((ans[i] - ans[i - 1] - a) % 26 + a)

    return ''.join(ans)


def decrypt2(word):
    if not word:
        return ''

    a = ord('a')
    ans = [ord(c) for c in word]
    cumul = 1

    for i in range(len(word)):
        # substract the cumul sum
        ans[i] -= cumul

        # keep adding 26 to make ans[i] in [ord('a'), ord('z')]
        steps = (a - ans[i]) // 26
        if (a - ans[i]) % 26:
            # (a - ans[i]) % 26 != 0
            # add 1 more
            steps += 1
        ans[i] += steps * 26

        # update cumul
        cumul += ans[i]
        ans[i] = chr(ans[i])

    return ''.join(ans)
