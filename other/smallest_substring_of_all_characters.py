def get_shortest_unique_substring(strs, s):
    if not strs or not s:
        return ''

    freq = dict.fromkeys(strs, 0)
    left = cnt = 0
    start = 0
    size = INF = float('inf')

    for right in range(len(s)):
        if s[right] in freq:
            if freq[s[right]] == 0:
                cnt += 1
            freq[s[right]] += 1

        while cnt == len(freq):
            if right - left + 1 < size:
                start = left
                size = right - left + 1

            if s[left] in freq:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    cnt -= 1

            left += 1

    return s[start:start + size] if size < INF else ''
