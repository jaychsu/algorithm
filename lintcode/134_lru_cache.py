"""
Main Concept:

Dm <-> a <-> b <-> c <-> dm  |<- cache_list (dll)

1. if cache is updated (set/get)
    => move to the end of cache_list
2. if cache is full
    => evict the most left node in cache first,
       that is `a` in above diagram
    => add the new cache to the end of the cache_list as new tail
"""


class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.cap = capacity
        self.nodes = {}
        self.D = CacheNode(-1)
        self.d = CacheNode(-1)
        self.D.nxt = self.d
        self.d.pre = self.D

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.nodes:
            return -1

        self._update(key)
        return self.nodes[key].val

    def set(self, key, val):
        """
        :type key: int
        :type val: int
        :rtype: void
        """
        if self.cap <= 0:
            return

        if key in self.nodes:
            self._update(key, val)
            return

        while len(self.nodes) >= self.cap:
            self._evict()

        self._add(key, val)

    def _evict(self):
        node = self._pop_head()
        del self.nodes[node.key]

    def _update(self, key, val=None):
        node = self.nodes[key]

        if val:
            node.val = val

        node.unlink()
        self._add_tail(node)

    def _add(self, key, val):
        self.nodes[key] = CacheNode(key, val)
        self._add_tail(self.nodes[key])

    def _pop_head(self):
        node = self.D.nxt
        node.unlink()
        return node

    def _add_tail(self, node):
        node.link(self.d.pre, self.d)


class CacheNode:
    def __init__(self, key, val=None, pre=None, nxt=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.nxt = nxt

    def link(self, pre, nxt):
        self.pre = pre
        self.nxt = nxt
        pre.nxt = self
        nxt.pre = self

    def unlink(self):
        self.pre.nxt = self.nxt
        self.nxt.pre = self.pre
        self.pre = self.nxt = None
