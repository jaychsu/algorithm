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
Dummy Tail Doubly Linked List
"""
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.recent = DoublyLinkedList()

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
        self.recent.append_tail(cache_node)

    def _evict_item(self):
        cache_node = self.recent.pop_head()
        self.cache.pop(cache_node.key)

    def _update_item(self, key, val=None):
        cache_node = self.cache[key]

        if val:
            cache_node.val = val

        self.recent.append_tail(cache_node)


class CacheNode:
    def __init__(self, key, val=None, pre=None, nxt=None):
        self.pre = pre
        self.nxt = nxt
        self.key = key
        self.val = val

    def unlink(self):
        if self.pre:
            self.pre.nxt = self.nxt
        if self.nxt:
            self.nxt.pre = self.pre

        self.pre = self.nxt = None


class DoublyLinkedList:
    def __init__(self):
        self.dummy = self.tail = CacheNode(-1)

    def get_head(self):
        return self.dummy.nxt

    def get_tail(self):
        if self.dummy is self.tail:
            return

        return self.tail

    def pop_head(self):
        if self.dummy is self.tail:
            return

        head = self.dummy.nxt
        if head is self.tail:
            self.tail = self.dummy

        head.unlink()
        return head

    def append_tail(self, cache_node):
        if cache_node is self.tail:
            return

        cache_node.unlink()
        cache_node.pre = self.tail
        self.tail.nxt = cache_node
        self.tail = cache_node


# =========================================
"""
Cyclic Doubly Linked List
"""
class LRUCache:
    """
    @param: capacity: An integer
    """
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.recent = DoublyLinkedList()

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
        _, _, item = self.cache[key]
        return item['val']

    def _add_item(self, key, val):
        node = self.recent.new_node(key=key, val=val)
        self.recent.append_tail(node)
        self.cache[key] = node

    def _evict_item(self):
        _, _, item = self.recent.pop_head()
        self.cache.pop(item['key'])

    def _update_item(self, key, val=None):
        node = self.cache[key]

        if val:
            node[2]['val'] = val

        self.recent.unlink(node)
        self.recent.append_tail(node)


class DoublyLinkedList:
    def __init__(self, **kw):
        head, _len = None, 0

        if kw:
            head = []
            head[:] = self.new_node(head, head, **kw)
            _len = 1

        self.head = head
        self._len = _len

    def new_node(self, pre=None, nxt=None, **kw):
        return [pre, nxt, kw]

    def pop_head(self):
        if self._len == 0:
            return self.head

        if self._len == 1:
            head = self.head
            self.head = None
            self._len = 0
            return head

        return self.unlink(self.head)

    def append_tail(self, node):
        if self._len == 0:
            node[:] = self.new_node(node, node, **node[2])
            self.head = node
            self._len = 1
            return node

        tail, _, _ = head = self.head
        tail[1] = head[0] = node
        node[0] = tail
        node[1] = head
        self._len += 1
        return node

    def unlink(self, node):
        pre, nxt, _ = node
        pre[1] = nxt
        nxt[0] = pre
        node[0] = node[1] = None

        if node is self.head:
            self.head = nxt

        self._len -= 1

        if self._len == 0:
            self.head = None

        return node

    def __str__(self):
        return ' <-> '.join([
            str(item)
            for _, _, item in self.__iter__()
        ])

    def __iter__(self):
        node = self.head
        while node:
            _, nxt, _ = node
            yield node

            if nxt is self.head:
                break

            node = nxt

    def __bool__(self):
        return self._len > 0

    def __repr__(self):
        return repr(self.head)

    def __len__(self):
        return self._len
