class MemcacheItem:
    def __init__(self, value, expired_at):
        self.value = value
        self.expired_at = expired_at

INT_MAX = 2147483647

class Memcache:
    def __init__(self):
        self.cache = {}

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """
    def get(self, curtTime, key):
        if key not in self.cache:
            return INT_MAX
        item = self.cache[key]
        if any([
            item.expired_at >= curtTime,
            item.expired_at is -1,
        ]):
            return item.value
        else:
            return INT_MAX

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """
    def set(self, curtTime, key, value, ttl):
        if isinstance(ttl, int) and ttl > 0:
            item = MemcacheItem(value, curtTime + ttl - 1)
        else:
            item = MemcacheItem(value, -1)
        self.cache[key] = item

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """
    def delete(self, curtTime, key):
        if key not in self.cache:
            return
        del self.cache[key]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def incr(self, curtTime, key, delta):
        if key not in self.cache:
            return INT_MAX
        item = self.cache[key]
        if any([
            item.expired_at >= curtTime,
            item.expired_at is -1,
        ]):
            item.value += delta
            return item.value
        else:
            return INT_MAX

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def decr(self, curtTime, key, delta):
        return self.incr(curtTime, key, delta * -1)
