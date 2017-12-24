class Solution:
    """
    @param: s: a string
    @param: D: a set of n substrings
    @return: the minimum length
    """
    def minLength(self, s, D):
        if not s:
            return 0

        _min = len(s)
        queue = [s]
        visited = set([s])

        """
        bfs
                 s
          /----/---\----\
        s-d1 s-d2 s-d3 s-d4
        ...  ...  ...  ...
        """
        for s in queue:
            for d in D:
                found = s.find(d)
                while found != -1:
                    _s = s[:found] + s[found + len(d):]
                    found = s.find(d, found + 1)

                    if _s in visited:
                        continue

                    if len(_s) < _min:
                        _min = len(_s)

                    queue.append(_s)
                    visited.add(_s)

        return _min
