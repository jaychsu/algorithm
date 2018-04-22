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
... ):
...     res = encrypt(origin)
...     if res != encryption: print('L14', origin, res)
...     gotcha.append(res == encryption)
...     res = decrypt(encryption)
...     if res != origin: print('L17', encryption, res)
...     gotcha.append(res == origin)
...     res = decrypt(encrypt(origin))
...     if res != origin: print('L20', origin, res)
...     gotcha.append(res == origin)
>>> bool(gotcha) and all(gotcha)
True
"""


def encrypt(word):
    n = len(word)
    a = ord('a')
    ans = [ord(c) for c in word]
    cumul = 1

    for i in range(n):
        cumul += ans[i]
        ans[i] = chr((cumul - a) % 26 + a)

    return ''.join(ans)


def decrypt(word):
    n = len(word)
    a = ord('a')
    ans = [ord(c) for c in word]
    cumul = 1

    for i in range(n):
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
