from collections import OrderedDict

class LFUCache:
    """
    For a cache with capacity k, if the cache is full and need to evict a key in it,
    the key with:
    1. lower frequency of use
    2. earlier time to save to cache
    will be kicked out.

    this solution is not good, since the time complexity is quite high.
    """

    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        if capacity < 1:
            return
        self.capacity = capacity
        self.freqs = OrderedDict()
        self.cache = {}

    """
    @param: key: An integer
    @param: value: An integer
    @return: nothing
    """
    def set(self, key, value):
        if key in self.cache:
            self.cache[key] = value
            self.freqs[key] += 1
            return
        if len(self.cache) >= self.capacity:
            lowest_freq = min(self.freqs.values())
            results = [item for item in self.freqs.items() if item[1] <= lowest_freq]
            target_key = results[0][0]
            del self.cache[target_key]
            del self.freqs[target_key]
        self.cache[key] = value
        self.freqs[key] = 0

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key in self.cache:
            freq = self.freqs[key] + 1
            del self.freqs[key]
            self.freqs[key] = freq
            # # python 3
            # self.freqs[key] += 1
            # self.freqs.move_to_end(key)
            return self.cache[key]
        return -1
