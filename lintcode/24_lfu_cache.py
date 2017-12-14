"""
Main Concept:

dummy <-> 2 <-> 3 <-> 8   |<- freq_list (dll)
          |     |     |
          a     c     d   |<- cache_list (dll)
          &           &
          b           e

1. if cache is updated (set/get)
    => freq += 1
    => move to the end of the cache_list in new freq_list
2. if cache is full
    => evict the most top-left in cache first,
       that is `a` in above diagram
    => add the new cache to the end of the cache_list in freq `0`
"""


"""
Two Dummy Doubly Linked List
"""
class LFUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.D = FreqNode(-1)
        self.d = FreqNode(-1)
        self.D.nxt, self.d.pre = self.d, self.D

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

        freq_head = self.D.nxt
        if freq_head and freq_head.freq == 0:
            freq_head.append_tail(cache_node)
            return

        freq_head = FreqNode(0)
        freq_head.append_tail(cache_node)
        self.D.after(freq_head)

    def _evict_item(self):
        freq_head = self.D.nxt
        cache_node = freq_head.pop_head()
        self.cache.pop(cache_node.key)

        if freq_head.is_empty():
            freq_head.unlink()

    def _update_item(self, key, val=None):
        cache_node = self.cache[key]

        if val:
            cache_node.val = val

        from_freq = cache_node.freq_node
        to_freq = None

        if from_freq.nxt and from_freq.nxt.freq == from_freq.freq + 1:
            to_freq = from_freq.nxt
        else:
            to_freq = FreqNode(from_freq.freq + 1)
            from_freq.after(to_freq)

        cache_node.unlink()
        to_freq.append_tail(cache_node)

        if from_freq.is_empty():
            from_freq.unlink()


class CacheNode:
    def __init__(self, key, val=None, freq_node=None, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.freq_node = freq_node
        self.pre = pre
        self.nxt = nxt

    # to change self in cache nodes
    def unlink(self):
        self.pre.nxt = self.nxt
        self.nxt.pre = self.pre

        self.pre = self.nxt = self.freq_node = None


class FreqNode:
    def __init__(self, freq, pre=None, nxt=None):
        self.freq = freq
        self.pre = pre
        self.nxt = nxt
        self.D = CacheNode(-1)
        self.d = CacheNode(-1)
        self.D.nxt, self.d.pre = self.d, self.D

    # to change self in freq nodes
    def unlink(self):
        self.pre.nxt = self.nxt
        self.nxt.pre = self.pre

        self.pre = self.nxt = self.D = self.d = None

    # to change self in freq nodes
    def after(self, node):
        node.pre = self
        node.nxt = self.nxt
        self.nxt.pre = node
        self.nxt = node

    # to manage cache nodes
    def is_empty(self):
        return self.D.nxt is self.d

    # to manage cache nodes
    def pop_head(self):
        if self.is_empty():
            return

        head = self.D.nxt
        head.unlink()
        return head

    # to manage cache nodes
    def append_tail(self, node):
        node.freq_node = self
        node.pre = self.d.pre
        node.nxt = self.d
        self.d.pre.nxt = node
        self.d.pre = node
