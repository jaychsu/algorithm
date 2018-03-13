"""
D <-> x <-> y <-> z <-> D
"""
import collections
from linked_list.python._helper import *


class CyclicDoublyList(ListBase):
    def __init__(self):
        self.clear()

    def __iter__(self):
        node = self.__dummy[2]
        while node is not self.__dummy:
            obj, _, nxt = node
            yield obj
            node = nxt

    def set(self, obj, index=-1):
        self._check_index(index, raise_error=True)
        target = self._get_node(index)
        target[0] = obj
        return obj

    def get(self, index=-1):
        self._check_index(index, raise_error=True)
        return self._get_node(index)[0]

    def add(self, obj, index=-1):
        if not self._check_index(index):
            index = -1

        target = self._get_node(index)
        if index < 0:
            node = self._new_node(obj, target, target[2])
            target[2][1] = node
            target[2] = node
        else:
            node = self._new_node(obj, target[1], target)
            target[1][2] = node
            target[1] = node

        self.__size += 1

    def add_all(self, objs, index=-1):
        if not isinstance(objs, collections.Iterable):
            raise ValueError('Oops! passed-in objs was not iterable.')

        if not self._check_index(index):
            index = -1

        dummy = tail = self._new_node(None)
        for obj in objs:
            tail[2] = self._new_node(obj, tail)
            tail = tail[2]

        target = self._get_node(index)
        if index < 0:
            dummy[2][1] = target
            tail[2] = target[2]
            target[2][1] = tail
            target[2] = dummy[2]
        else:
            dummy[2][1] = target[1]
            tail[2] = target
            target[1][2] = dummy[2]
            target[1] = tail

        self.__size += len(objs)

    def remove(self, index=-1):
        self._check_index(index, raise_error=True)
        obj, pre, nxt = self._get_node(index)
        pre[2] = nxt
        nxt[1] = pre

        self.__size -= 1
        return obj

    def contains(self, obj):
        for node in self.__iter__():
            if node is obj:
                return True

        return False

    def index(self, obj):
        i = 0
        node = self.__dummy[2]
        while node is not self.__dummy:
            if node[0] is obj:
                return i
            node = node[2]
            i += 1
        return -1

    def last_index(self, obj):
        i = 1
        node = self.__dummy[1]
        while node is not self.__dummy:
            if node[0] is obj:
                return i
            node = node[1]
            i += 1
        return -1

    def clear(self):
        dummy = []
        dummy[:] = self._new_node(None, dummy, dummy)
        self.__dummy = dummy
        self.__size = 0

    def clone(self):
        pass

    def sort(self, key=None):
        pass

    def _get_size(self):
        return self.__size

    def _get_node(self, index=-1):
        node = None

        if index < 0:
            i = -index
            node = self.__dummy
            while i != 0:
                i -= 1
                node = node[1]
        else:
            i = index
            node = self.__dummy[2]
            while i != 0:
                i -= 1
                node = node[2]

        return node

    def _new_node(self, obj, pre=None, nxt=None):
        return [obj, pre, nxt]
