"""
h                 h
x --> y --> z --> x

h                 h
x <-> y <-> z <-> x
"""


class LinkedList:
    # TODO
    pass


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

    def append_before(self, a, b):
        # c <-> a => c <-> b <-> a
        # note that, b MUST BE no relation with other
        # or `self.unlink(b)` outside first
        c, _, _ = a

        c[1] = a[0] = b
        b[0] = c
        b[1] = a

        if a is self.head:
            self.head = b

        self._len += 1
        return b

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

    def sort(self):
        # TODO
        pass

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

    def __getitem__(self, key):
        # TODO
        pass

    def __setitem__(self, key, val):
        # TODO
        pass
