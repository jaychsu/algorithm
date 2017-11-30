class Memcache:

    INT_MAX = 0x7FFFFFFF
    PERMANENT_TTL = -1
    storage = {}

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: An integer
    """
    def get(self, curtTime, key):
        if key not in self.storage:
            return self.INT_MAX

        if (curtTime < self.storage[key]['expired_at'] or
            self.storage[key]['expired_at'] == self.PERMANENT_TTL):
            return self.storage[key]['val']

        return self.INT_MAX

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: value: An integer
    @param: ttl: An integer
    @return: nothing
    """
    def set(self, curtTime, key, value, ttl):
        if ttl > 0:
            self.storage[key] = self._new_item(key, value, curtTime + ttl)
        else:
            self.storage[key] = self._new_item(key, value, self.PERMANENT_TTL)

    """
    @param: curtTime: An integer
    @param: key: An integer
    @return: nothing
    """
    def delete(self, curtTime, key):
        if key in self.storage:
            del self.storage[key]

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def incr(self, curtTime, key, delta):
        if key not in self.storage:
            return self.INT_MAX

        if (curtTime < self.storage[key]['expired_at'] or
            self.storage[key]['expired_at'] == self.PERMANENT_TTL):
            self.storage[key]['val'] += delta
            return self.storage[key]['val']

        return self.INT_MAX

    """
    @param: curtTime: An integer
    @param: key: An integer
    @param: delta: An integer
    @return: An integer
    """
    def decr(self, curtTime, key, delta):
        return self.incr(curtTime, key, -1 * delta)

    def _new_item(self, key, value, expired_at):
        return {
            'key': key,
            'val': value,
            'expired_at': expired_at
        }
