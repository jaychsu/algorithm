class HashTable:
    def __init__(self, cap=4000, power=31):
        self.cap = cap
        self.power = power
        self.size = 0
        self.table = [None] * self.cap

    def __repr__(self):
        return '{{{}}}'.format(
            ', '.join(
                repr(key) + ': ' + repr(val)
                for key, val in self.items()
            )
        )

    def __len__(self):
        return self.size

    def __setitem__(self, key, val):
        self.set(key, val)

    def __getitem__(self, key):
        return self.get(key)

    def __delitem__(self, key):
        self.remove(key)

    def __iter__(self):
        for key, _ in self.items():
            yield key

    def keys(self):
        for key, _ in self.items():
            yield key

    def values(self):
        for _, val in self.items():
            yield val

    def items(self):
        for head in self.table:
            node = head

            while node:
                yield node.key, node.val
                node = node.nxt

    def set(self, key, val):
        code = self._encode(key)

        if not self.table[code]:
            self.size += 1
            self.table[code] = ListNode(key, val)
            return

        node = self.table[code]

        while node and node.nxt and node.key != key:
            node = node.nxt

        if node.key == key:
            node.val = val
        else:
            self.size += 1
            node.nxt = ListNode(key, val)

    def get(self, key):
        code = self._encode(key)

        if not self.table[code]:
            raise KeyError(key)

        node = self.table[code]

        while node and node.key != key:
            node = node.nxt

        if node and node.key == key:
            return node.val

        raise KeyError(key)

    def remove(self, key):
        code = self._encode(key)

        if not self.table[code]:
            raise KeyError(key)

        if self.table[code].key == key:
            self.size -= 1
            self.table[code] = self.table[code].nxt
            return

        node = self.table[code]

        while node and node.nxt and node.nxt.key != key:
            node = node.nxt

        if node and node.nxt and node.nxt.key == key:
            self.size -= 1
            node.nxt = node.nxt.nxt
            return

        raise KeyError(key)

    def _encode(self, key):
        if isinstance(key, int):
            return key % self.cap

        code = 0

        for c in key:
            code = (code * self.power + ord(c)) % self.cap

        return code


class ListNode:
    def __init__(self, key, val, nxt=None):
        self.key = key
        self.val = val
        self.nxt = nxt
