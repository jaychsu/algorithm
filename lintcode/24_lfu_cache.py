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

TODO:

- change the structure of cache_list from `head-tail` to `dummy-tail`
"""


class LFUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.freq_dummy = FreqNode(-1)

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

        head = self.freq_dummy.nxt

        # if the minimum `freq_node` is just `0`
        if head and head.freq == 0:
            head.append_tail(cache_node)
            return

        # if the minimum `freq_node` is not `0`
        head = FreqNode(0)
        head.append_tail(cache_node)
        self.freq_dummy.after(head)

    def _evict_item(self):
        head = self.freq_dummy.nxt
        key = head.cache_head.key
        self.cache.pop(key)

        head.pop_head()

        if head.is_empty():
            head.unlink()

    def _update_item(self, key, val=None):
        cache_node = self.cache[key]

        if val:
            cache_node.val = val

        from_freq = cache_node.dummy
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
    def __init__(self, key, val, dummy=None, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.dummy = dummy
        self.pre = pre
        self.nxt = nxt

    def unlink(self):
        head = self.dummy.cache_head
        tail = self.dummy.cache_tail

        if self is head and self is tail:
            self.dummy.cache_head = self.dummy.cache_tail = None
        elif self is head:
            self.dummy.cache_head = self.nxt
            self.nxt.pre = None
        elif self is tail:
            self.pre.nxt = None
            self.dummy.cache_tail = self.pre
        else:
            self.pre.nxt = self.nxt
            self.nxt.pre = self.pre

        self.pre = self.nxt = self.dummy = None


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
        # no nodes
        if self.is_empty():
            return

        # 1 node
        head = self.cache_head
        if head is self.cache_tail:
            self.cache_head = self.cache_tail = None
            return head

        # 2+ nodes
        self.cache_head = head.nxt
        head.nxt.pre = None
        return head

    def append_tail(self, cache_node):
        # the passed node MUST BE no relation with other

        cache_node.dummy = self

        if self.is_empty():
            self.cache_head = self.cache_tail = cache_node
            return

        cache_node.pre = self.cache_tail
        self.cache_tail.nxt = cache_node
        self.cache_tail = cache_node

    def after(self, freq_node):
        if self.nxt:
            self.nxt.pre = freq_node

        freq_node.pre = self
        freq_node.nxt = self.nxt
        self.nxt = freq_node
