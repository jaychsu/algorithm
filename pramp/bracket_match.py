def bracket_match(text):
    ans = 0
    if not text:
        return ans

    cnt = 0

    for c in text:
        if c == '(':
            cnt += 1
        elif c == ')':
            cnt -= 1

        if cnt < 0:
            cnt = 0
            ans += 1

    if cnt > 0:
        ans += cnt

    return ans
