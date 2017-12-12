"""
Main Concept:

head <-> 2 <-> 3 <-> 8   |<- freq_list (dll)
         &     &     &   |<- cache_list (dll)
         a     c     d
         &           &
         b           e

1. if cache is updated (set/get)
    => freq += 1
    => move to the tail of cache_list
2. if cache is full
    => evict the top-left cache first, that is `a` in above diagram
    => add the new cache to the tail of `1` in cache_list
"""


class LFUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.freq_dummy = None

    """
    @param: key: An integer
    @param: val: An integer
    @return: nothing
    """
    def set(self, key, val):
        if self.capacity <= 0:
            return

        if key in self.cache:
            self._update_item(key, val)
            return

        if len(self.cache) >= self.capacity:
            self._evict_item()

        self._add_item(key, val)

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.cache:
            return -1

        self._update_item(key)
        return self.cache[key].val

    def _add_item(self, key, val):
        cache_node = CacheNode(key, val)
        self.cache[key] = cache_node

        if not self.freq_dummy:
            self.freq_dummy = FreqNode(0)
            self.freq_dummy.append_tail(cache_node)
            return

        if self.freq_dummy.freq == 0:
            self.freq_dummy.append_tail(cache_node)
            return

        freq_node = FreqNode(0)
        freq_node.append_tail(cache_node)
        self.freq_dummy.before(freq_node)
        self.freq_dummy = freq_node

    def _evict_item(self):
        freq_dummy = self.freq_dummy
        key = freq_dummy.cache_head.key
        self.cache.pop(key)
        freq_dummy.pop_head()

        if freq_dummy.is_empty():
            self.freq_dummy = freq_dummy.nxt
            freq_dummy.unlink()

    def _update_item(self, key, val=None):
        cache_node = self.cache[key]
        freq_node = cache_node.cache_dummy
        target_freq_node = None

        if val:
            cache_node.val = val

        if (not freq_node.nxt or
            freq_node.nxt.freq != freq_node.freq + 1):
            target_freq_node = FreqNode(freq_node.freq + 1)
            freq_node.after(target_freq_node)
        else:
            target_freq_node = freq_node.nxt

        cache_node.unlink()
        target_freq_node.append_tail(cache_node)

        if freq_node.is_empty():
            if self.freq_dummy is freq_node:
                self.freq_dummy = target_freq_node
            freq_node.unlink()


class CacheNode:
    def __init__(self, key, val, cache_dummy=None, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.cache_dummy = cache_dummy
        self.pre = pre
        self.nxt = nxt

    def unlink(self):
        if self.cache_dummy.cache_head is self.cache_dummy.cache_tail:
            self.cache_dummy.cache_head = self.cache_dummy.cache_tail = None
        elif self.cache_dummy.cache_head is self:
            self.cache_dummy.cache_head = self.nxt
            self.nxt.pre = None
        elif self.cache_dummy.cache_tail is self:
            self.pre.nxt = None
            self.cache_dummy.cache_tail = self.pre
        else:
            self.pre.nxt = self.nxt
            self.nxt.pre = self.pre

        self.pre = self.nxt = self.cache_dummy = None


class FreqNode:
    def __init__(self, freq, pre=None, nxt=None):
        self.freq = freq
        self.pre = pre
        self.nxt = nxt
        self.cache_head = None
        self.cache_tail = None

    def is_empty(self):
        return not self.cache_head and not self.cache_tail

    def unlink(self):
        if self.pre:
            self.pre.nxt = self.nxt
        if self.nxt:
            self.nxt.pre = self.pre

        self.pre = self.nxt = self.cache_head = self.cache_tail = None

    def pop_head(self):
        if self.is_empty():
            return

        if self.cache_head is self.cache_tail:
            cache_node = self.cache_head
            self.cache_head = self.cache_tail = None
            return cache_node

        cache_node = self.cache_head
        self.cache_head = cache_node.nxt
        cache_node.nxt.pre = None
        return cache_node

    def append_tail(self, cache_node):
        cache_node.cache_dummy = self

        if self.is_empty():
            self.cache_head = self.cache_tail = cache_node
            return

        cache_node.pre = self.cache_tail
        cache_node.nxt = None
        self.cache_tail.nxt = cache_node
        self.cache_tail = cache_node

    def before(self, freq_node):
        if self.pre:
            self.pre.nxt = freq_node

        freq_node.pre = self.pre
        freq_node.nxt = self
        self.pre = freq_node

    def after(self, freq_node):
        if self.nxt:
            self.nxt.pre = freq_node

        freq_node.pre = self
        freq_node.nxt = self.nxt
        self.nxt = freq_node
