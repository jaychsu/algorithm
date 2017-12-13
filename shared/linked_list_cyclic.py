"""
x --> y --> z --> x

x <-> y <-> z <-> x
"""


class LinkedList:
    # TODO
    pass


class DoublyLinkedList:
    def __init__(self, val=None):
        head = []
        head[:] = [head, head, val]
        self.head = head
        self._len = 1 if val else 0

    def pop_head(self):
        # TODO
        pass

    def append_tail(self, val):
        if self._len is 0:
            self.head[2] = val
            self._len = 1
            return self.head

        tail = self.head[0]
        node = [tail, self.head, val]
        tail[1] = self.head[0] = node
        self._len += 1
        return node

    def before(self):
        # TODO
        pass

    def after(self):
        # TODO
        pass

    def unlink(self, node):
        pre, nxt, _ = node
        pre[1] = nxt
        nxt[0] = pre
        return node

    def sort(self):
        # TODO
        pass

    def __repr__(self):
        return repr(self.head)

    def __str__(self):
        return ' <-> '.join([str(val) for val in self.__iter__()])

    def __len__(self):
        return self._len

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr[2]

            if curr[1] is self.head:
                break

            curr = curr[1]

    def __getitem__(self, key):
        # TODO
        pass

    def __setitem__(self, key, val):
        # TODO
        pass
