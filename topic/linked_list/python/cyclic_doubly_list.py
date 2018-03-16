"""
D <-> x <-> y <-> z <-> D
"""
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
        """
        :type obj: any
        :type index: int
        :rtype: any
        """
        self._check_index(index, raise_error=True)
        target = self._get_node(index)
        target[0] = obj
        return obj

    def get(self, index=-1):
        """
        :type index: int
        :rtype: any
        """
        self._check_index(index, raise_error=True)
        return self._get_node(index)[0]

    def add(self, obj, index=-1):
        """
        :type obj: any
        :type index: int
        :rtype: void
        """
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
        """
        :type objs: Iterable
        :type index: int
        :rtype: void
        """
        super(CyclicDoublyList, self).add_all(objs, index)

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
        """
        :type index: int
        :rtype: any
        """
        self._check_index(index, raise_error=True)
        obj, pre, nxt = self._get_node(index)
        pre[2] = nxt
        nxt[1] = pre

        self.__size -= 1
        return obj

    def index(self, obj):
        """
        :type obj: any
        :rtype: int

        return -1 if not found
        """
        i = 0
        node = self.__dummy[2]

        while node is not self.__dummy:
            if node[0] is obj:
                return i
            node = node[2]
            i += 1

        return -1

    def last_index(self, obj):
        """
        :type obj: any
        :rtype: int

        return -1 if not found
        """
        i = 1
        node = self.__dummy[1]

        while node is not self.__dummy:
            if node[0] is obj:
                return i
            node = node[1]
            i += 1

        return -1

    def clear(self):
        """
        :rtype: void
        """
        dummy = []
        dummy[:] = self._new_node(None, dummy, dummy)
        self.__dummy = dummy
        self.__size = 0

    def clone(self):
        """
        :rtype: LinkedList
        """
        pass

    def sort(self, key=None):
        """
        :type key: function
        :rtype: void
        """
        pass

    def _get_size(self):
        """
        :rtype: int
        """
        return self.__size

    def _get_node(self, index=-1):
        """
        :type index: int
        :rtype: ListNode
        """
        node = None

        if index < 0:
            node = self.__dummy
            while index != 0:
                index += 1
                node = node[1]
        else:
            node = self.__dummy[2]
            while index != 0:
                index -= 1
                node = node[2]

        return node

    def _new_node(self, obj, pre=None, nxt=None):
        return [obj, pre, nxt]
