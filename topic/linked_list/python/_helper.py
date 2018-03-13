"""
api doc of Class java.util.LinkedList
https://courses.cs.washington.edu/courses/cse341/98au/java/jdk1.2beta4/docs/api/java/util/LinkedList.html
"""
from abc import ABC, abstractmethod


class ListNode:
    def __init__(self, val, nxt=None):
        self.val = val
        self.nxt = nxt


class DoublyListNode:
    def __init__(self, val, pre=None, nxt=None):
        self.val = val
        self.pre = pre
        self.nxt = nxt


class ListBase(ABC):
    def __repr__(self):
        return repr(self.to_array())

    def __str__(self):
        return str(self.to_array())

    def __bool__(self):
        return bool(self._get_size())

    def __len__(self):
        return self._get_size()


    def to_array(self):
        """
        :rtype: List[any]
        """
        return [obj for obj in self.__iter__()]

    def get_first(self):
        """
        :rtype: any
        """
        return self.get(0)

    def get_last(self):
        """
        :rtype: any
        """
        return self.get(-1)

    def add_first(self, obj):
        """
        :type obj: any
        :rtype: void
        """
        self.add(obj, 0)

    def add_last(self, obj):
        """
        :type obj: any
        :rtype: void
        """
        self.add(obj, -1)

    def remove_first(self):
        """
        :rtype: any
        """
        return self.remove(0)

    def remove_last(self):
        """
        :rtype: any
        """
        return self.remove(-1)

    def _check_index(self, index, raise_error=False):
        """
        :type index: int
        :type raise_error: bool
        :rtype: bool

        return True if index is valid
        return False if invalid and need silence
        raise IndexError if invalid and no need silence
        """
        size = self._get_size()

        if any((
            index >= 0 and index < size,
            index < 0 and -index <= size,
        )):
            # is valid
            return True

        if raise_error:
            raise IndexError('linked list index out of range')

        return False


    @abstractmethod
    def __iter__(self):
        pass

    @abstractmethod
    def _get_size(self):
        """
        :rtype: int
        """
        pass

    @abstractmethod
    def set(self, obj, index=-1):
        """
        :type obj: any
        :type index: int
        :rtype: any
        """
        pass

    @abstractmethod
    def get(self, index=-1):
        """
        :type index: int
        :rtype: any
        """
        pass

    @abstractmethod
    def add(self, obj, index=-1):
        """
        :type obj: any
        :type index: int
        :rtype: void
        """
        pass

    @abstractmethod
    def add_all(self, objs, index=-1):
        """
        :type objs: Iterable
        :type index: int
        :rtype: void
        """
        pass

    @abstractmethod
    def remove(self, index=-1):
        """
        :type index: int
        :rtype: any
        """
        pass


    @abstractmethod
    def contains(self, obj):
        """
        :type obj: any
        :rtype: bool
        """
        pass

    @abstractmethod
    def index(self, obj):
        """
        :type obj: any
        :rtype: int

        return -1 if not found
        """
        pass

    @abstractmethod
    def last_index(self, obj):
        """
        :type obj: any
        :rtype: int

        return -1 if not found
        """
        pass

    @abstractmethod
    def clear(self):
        """
        :rtype: void
        """
        pass

    @abstractmethod
    def clone(self):
        """
        :rtype: LinkedList
        """
        pass

    @abstractmethod
    def sort(self, key=None):
        """
        :type key: function
        :rtype: void
        """
        pass
