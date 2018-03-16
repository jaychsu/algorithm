"""
D --> x --> y --> z --> D

TODO: merge `_get_node`, `_get_prev_node`
"""
from linked_list.python._helper import *


class CyclicList(ListBase):
    def __init__(self):
        self.clear()

    def __iter__(self):
        node = self.__dummy[1]

        while node is not self.__dummy:
            obj, nxt = node
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

        target = None

        if index < 0:
            target = self._get_node(index)
        else:
            target = self._get_prev_node(index)

        node = self._new_node(obj, target[1])
        target[1] = node

        self.__size += 1

    def add_all(self, objs, index=-1):
        """
        :type objs: Iterable
        :type index: int
        :rtype: void
        """
        super(CyclicList, self).add_all(objs, index)

        if not self._check_index(index):
            index = -1

        dummy = tail = self._new_node(None)
        for obj in objs:
            tail[1] = self._new_node(obj)
            tail = tail[1]

        target = None

        if index < 0:
            target = self._get_node(index)
        else:
            target = self._get_prev_node(index)

        tail[1] = target[1]
        target[1] = dummy[1]

        self.__size += len(objs)

    def remove(self, index=-1):
        """
        :type index: int
        :rtype: any
        """
        self._check_index(index, raise_error=True)
        node = self._get_prev_node(index)
        obj = node[1][0]
        node[1] = node[1][1]

        self.__size -= 1
        return obj

    def index(self, obj):
        """
        :type obj: any
        :rtype: int

        return -1 if not found
        """
        i = 0
        node = self.__dummy[1]

        while node is not self.__dummy:
            if node[0] is obj:
                return i
            node = node[1]
            i += 1

        return -1

    def last_index(self, obj):
        """
        :type obj: any
        :rtype: int

        return -1 if not found
        """
        head = node = self.__dummy[1]

        while node[0] is not obj:
            if node[1] is head:
                return -1

            node = node[1]

        i = 0

        while node[1] is not head:
            node = node[1]
            i += 1

        return i

    def clear(self):
        """
        :rtype: void
        """
        dummy = []
        dummy[:] = self._new_node(None, dummy)
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
        head = slow = self.__dummy[1]

        if index < 0:
            fast = head
            while index != 0:
                index += 1
                fast = fast[1]
            while fast[1] is not head:
                slow = slow[1]
                fast = fast[1]
        else:
            while index != 0:
                index -= 1
                slow = slow[1]

        return slow

    def _get_prev_node(self, index=-1):
        """
        :type index: int
        :rtype: ListNode

        This method may return dummy
        """
        dummy = slow = self.__dummy

        if index < 0:
            fast = dummy
            while index != 0:
                index += 1
                fast = fast[1]
            while fast[1] is not dummy:
                slow = slow[1]
                fast = fast[1]
        else:
            while index != 0:
                index -= 1
                slow = slow[1]

        return slow

    def _new_node(self, obj, nxt=None):
        return [obj, nxt]
