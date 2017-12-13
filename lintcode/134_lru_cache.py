"""
Main Concept:

dummy <-> a <-> b <-> c  |<- cache_list (dll)

1. if cache is updated (set/get)
    => move to the end of cache_list
2. if cache is full
    => evict the most left node in cache first,
       that is `a` in above diagram
    => add the new cache to the end of the cache_list as new tail
"""


class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.dummy = self.tail = CacheNode(-1, -1)

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

        self._append_tail(cache_node)

    def _evict_item(self):
        key = self.dummy.nxt.key
        self.cache.pop(key)

        self._pop_head()

    def _update_item(self, key, val=None):
        cache_node = self.cache[key]

        if val:
            cache_node.val = val

        self._append_tail(cache_node)

    def _pop_head(self):
        # no nodes
        if self.dummy is self.tail:
            return

        # 1 node
        head = self.dummy.nxt
        if head is self.tail:
            self.dummy.nxt = None
            self.tail = self.dummy
            return head

        # 2+ nodes
        head.relink()
        return head

    def _append_tail(self, cache_node):
        # passed node is already at end
        if cache_node is self.tail:
            return

        cache_node.relink(pre=self.tail)
        self.tail.nxt = cache_node
        self.tail = cache_node


class CacheNode:
    def __init__(self, key, val, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.nxt = nxt

    def relink(self, pre=None, nxt=None):
        if self.pre:
            self.pre.nxt = self.nxt
        if self.nxt:
            self.nxt.pre = self.pre

        self.pre, self.nxt = pre, nxt
