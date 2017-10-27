class MemcacheItem:
    def __init__(self, key, value, expired_at):
        self.key = key
        self.value = value
        self.expired_at = expired_at

class Memcache:
    def __init__(self):
        self.cache = {}
        self.MAX_INT = 2147483647

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """
    def get(self, curtTime, key):
        if key not in self.cache:
            return self.MAX_INT
        item = self.cache[key]
        if item.expired_at >= curtTime \
            or item.expired_at is -1:
            return item.value
        return self.MAX_INT

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """
    def set(self, curtTime, key, value, ttl):
        if isinstance(ttl, int) \
            and ttl > 0:
            self.cache[key] = MemcacheItem(key, value, curtTime + ttl - 1)
        else:
            self.cache[key] = MemcacheItem(key, value, -1)

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """
    def delete(self, curtTime, key):
        if key in self.cache:
            del self.cache[key]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def incr(self, curtTime, key, delta):
        if key not in self.cache:
            return self.MAX_INT
        item = self.cache[key]
        if item.expired_at >= curtTime \
            or item.expired_at is -1:
            item.value += delta
            return item.value
        return self.MAX_INT

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def decr(self, curtTime, key, delta):
        return self.incr(curtTime, key, delta * -1)
