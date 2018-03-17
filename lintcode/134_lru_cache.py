"""
Main Concept:

dummy <-> a <-> b <-> c <-> dummy  |<- cache_list (dll)

1. if cache is updated (set/get)
    => move to the end of cache_list
2. if cache is full
    => evict the most left node in cache first,
       that is `a` in above diagram
    => add the new cache to the end of the cache_list as new tail
"""


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

    def link(self, pre_node, nxt_node):
        self.pre = pre_node
        self.nxt = nxt_node
        pre_node.nxt = self
        nxt_node.pre = self


class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.cap = capacity
        self.nodes = {}

        self.D = CacheNode(-1)
        self.d = CacheNode(-1)
        self.D.nxt = self.d
        self.d.pre = self.D

    """
    @param: key: An integer
    @return: An integer
    """
    def get(self, key):
        if key not in self.nodes:
            return -1

        self._update_item(key)
        return self.nodes[key].val

    """
    @param: key: An integer
    @param: val: An integer
    @return: nothing
    """
    def set(self, key, val):
        if self.cap <= 0:
            return

        if key in self.nodes:
            self._update_item(key, val)
            return

        while len(self.nodes) >= self.cap:
            self._evict_item()

        self._add_item(key, val)

    def _evict_item(self):
        node = self._pop_head()
        del self.nodes[node.key]

    def _add_item(self, key, val):
        self.nodes[key] = CacheNode(key, val)
        self._add_tail(self.nodes[key])

    def _update_item(self, key, val=None):
        node = self.nodes[key]

        if val:
            node.val = val

        node.unlink()
        self._add_tail(node)

    def _pop_head(self):
        node = self.D.nxt
        node.unlink()
        return node

    def _add_tail(self, node):
        node.link(self.d.pre, self.d)
