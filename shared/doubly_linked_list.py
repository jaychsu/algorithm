class DoublyLinkedList:
    def __init__(self, val=None):
        head = []
        head[:] = [head, head, val]
        self.head = head

    def append(self, val):
        tail = self.head[0]
        node = [tail, self.head, val]
        tail[1] = self.head[0] = node
        return node

    def remove(self, node):
        pre, nxt, _ = node
        pre[1] = nxt
        nxt[0] = pre
        return node

    def get_tail(self):
        return self.head[0]

    def sort(self):
        # TODO
        pass

    def __repr__(self):
        return repr(self.head)

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr[2]

            if curr[1] is self.head:
                break

            curr = curr[1]

    def __getitem__(self, key):
        return self.head[key]

    def __setitem__(self, key, val):
        self.head[key] = val
