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


"""
Two Dummy Doubly Linked List
"""
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.caches = {}
        self.D = CacheNode(-1)
        self.d = CacheNode(-1)
        self.D.nxt, self.d.pre = self.d, self.D

    """
    @param: key: An integer
    @param: val: An integer
    @return: nothing
    """
    def set(self, key, val):
        if self.capacity <= 0:
            return

        if key in self.caches:
            self._update_item(key, val)
            return

        if len(self.caches) >= self.capacity:
            self._evict_item()

        self._add_item(key, val)

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.caches:
            return -1

        self._update_item(key)
        return self.caches[key].val

    def _add_item(self, key, val):
        cache_node = CacheNode(key, val)
        self.caches[key] = cache_node
        self.append_tail(cache_node)

    def _evict_item(self):
        head = self.pop_head()
        self.caches.pop(head.key)

    def _update_item(self, key, val=None):
        cache_node = self.caches[key]

        if val:
            cache_node.val = val

        cache_node.unlink()
        self.append_tail(cache_node)

    def is_empty(self):
        return self.D.nxt is self.d

    def pop_head(self):
        if self.is_empty():
            return

        head = self.D.nxt
        head.unlink()
        return head

    def append_tail(self, cache_node):
        cache_node.pre = self.d.pre
        cache_node.nxt = self.d
        self.d.pre.nxt = cache_node
        self.d.pre = cache_node


class CacheNode:
    def __init__(self, key, val=None, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.nxt = nxt

    def unlink(self):
        self.pre.nxt = self.nxt
        self.nxt.pre = self.pre
        self.pre = self.nxt = None
