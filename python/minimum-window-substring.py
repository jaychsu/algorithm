class Solution:
    """
    @param: source : A string
    @param: target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source, target):
        if not source or not target:
            return ''
        n, m, freq_t, freq_s = len(source), len(target), dict.fromkeys(target, 0), {}
        begin = found = 0
        min_start, min_len, begin_char = -1, n, source[begin]
        for s in target: freq_t[s] += 1
        for end, child in enumerate(source):

            # Find the first matched window in current iteration
            freq_s[child] = freq_s.get(child, 0) + 1
            if freq_s[child] <= freq_t.get(child, 0):
                found += 1
            if found < m:
                continue

            # Move forward the left pointer to ignore those mismatched chars
            while begin < end and freq_s.get(begin_char, 0) > freq_t.get(begin_char, 0):
                freq_s[begin_char] = freq_s.get(begin_char, 0) - 1
                begin += 1
                begin_char = source[begin]

            # Record the length of current window if it less than min_len
            if end - begin < min_len: # actually should be `end + 1 - begin <= min_len` here, but it's equivalent
                min_len = end + 1 - begin
                min_start = begin

            # Start to find the next matched window
            found -= 1

        return '' if min_start is -1 else source[min_start : min_start + min_len]
