class Solution:
    """
    @param: source : A string
    @param: target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source, target):
        if not source or not target:
            return ''
        n, m = len(source), len(target)
        l = r = found = 0
        min_start, min_len = -1, n
        freq_s, freq_t = {}, dict.fromkeys(target, 0)
        for c in target: freq_t[c] += 1
        while r < n:
            # Find the first matched window in current iteration
            while r < n and found < m:
                freq_s[source[r]] = freq_s.get(source[r], 0) + 1
                if freq_s[source[r]] <= freq_t.get(source[r], 0):
                    found += 1
                r += 1

            # Terminate iteration if there is a string in source but not in target
            if r >= n and found < m:
                break

            # Move forward the left pointer to ignore those mismatched chars
            while l < r and freq_s[source[l]] > freq_t.get(source[l], 0):
                freq_s[source[l]] -= 1
                l += 1

            # Record the length of current window if it less than min_len
            if r - l <= min_len:
                min_start = l
                min_len = r - l

            # Start to find the next matched window
            freq_s[source[l]] -= 1
            found -= 1
        return '' if min_start == -1 else source[min_start : min_start + min_len]
