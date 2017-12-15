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
    nodes = None
    head = None

    def __init__(self, key=None, val=None):
        self.nodes = {}

        if not key or not val:
            # to create an empty DLL
            return

        head = []
        head[:] = self._create_node(key, val, head, head)
        self.nodes[key] = head
        self.head = head

    def get_head(self):
        if not self.head:
            return ()

        _, _, key, val = self.head
        return key, val

    def pop_head(self):
        if not self.head:
            return ()

        _, _, key, val = self.head
        self.remove(key)
        return key, val

    def prepend_head(self, key, val):
        if not self.head:
            return ()

        self._prepend(key, val, key=self.head[2], as_head=True)
        return key, val

    def get_tail(self):
        if not self.head:
            return ()

        _, _, key, val = self.head[0]
        return key, val

    def append_tail(self, key, val):
        if not self.head:
            return ()

        self._prepend(key, val, key=self.head[2])
        return key, val

    def pop_tail(self):
        if not self.head:
            return ()

        _, _, key, val = self.head[0]
        self.remove(key)
        return key, val

    def prepend(self, k_n, v_n, *, key=None, as_head=False):
        self._prepend(k_n, v_n, key=key, as_head=as_head)
        return k_n, v_n

    def append(self, k_n, v_n, *, key=None, as_head=False):
        # if `key` was no specific, or not in DLL
        # new node will append after `tail`

        if key and key in self.nodes:
            key = self.nodes[key][1][2]

        self._prepend(k_n, v_n, key=key, as_head=as_head)
        return k_n, v_n

    def remove(self, key):
        if not key or key not in self.nodes:
            return ()

        pre, nxt, _, val = node = self.nodes[key]
        pre[1] = nxt
        nxt[0] = pre
        node[0] = node[1] = None

        self.nodes.pop(key)

        if not self.nodes:
            self.head = None
            return key, val

        if node is self.head:
            self.head = nxt

        return key, val

    def sort(self):
        # TODO
        pass

    def _prepend(self, k_b, v_b, *, key=None, as_head=False):
        # c <-> a => c <-> b <-> a
        # if `key` was no specific, or not in DLL
        # new node_b will prepend before `head`

        if not self.nodes:
            b = []
            b[:] = self._create_node(k_b, v_b, b, b)
            self.nodes[k_b] = b
            self.head = b
            return k_b, v_b

        a = b = None

        if not key or key not in self.nodes:
            a = self.head
        else:
            a = self.nodes[key]

        if k_b in self.nodes:
            b = self.nodes[k_b]
            b[3] = v_b
            self.remove(k_b)
        else:
            b = self._create_node(k_b, v_b)

        c = a[0]
        c[1] = a[0] = b
        b[0] = c
        b[1] = a

        if as_head:
            self.head = b

        self.nodes[k_b] = b
        return k_b, v_b

    def _create_node(self, key, val, pre=None, nxt=None):
        return [pre, nxt, key, val]

    def __str__(self):
        if not self.nodes:
            return ''

        return '<- %s ->' % ' <-> '.join([
            str(kv_pair)
            for kv_pair in self.__iter__()
        ])

    def __iter__(self):
        node = self.head
        while node:
            _, nxt, k, v = node
            yield k, v

            if nxt is self.head:
                break

            node = nxt

    def __bool__(self):
        return bool(self.nodes)

    def __len__(self):
        return len(self.nodes)
