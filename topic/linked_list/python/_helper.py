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
    def __init__(self):
        pass

    def __repr__(self):
        pass

    def __str__(self):
        pass

    def __iter__(self):
        pass

    def __bool__(self):
        pass

    def __len__(self):
        pass


    @abstractmethod
    def set(self, obj, index=-1):
        pass

    @abstractmethod
    def get(self, index):
        pass

    @abstractmethod
    def add(self, obj, index=-1):
        pass

    @abstractmethod
    def add_all(self, objs, index=-1):
        pass

    @abstractmethod
    def remove(self, param):
        """
        if type(param) == int:
            index == param
        else:
            obj == param
        """
        pass


    @abstractmethod
    def contains(self, obj):
        pass

    @abstractmethod
    def index(self, obj):
        pass

    @abstractmethod
    def last_index(self, obj):
        pass

    @abstractmethod
    def clear(self):
        pass

    @abstractmethod
    def clone(self):
        pass

    @abstractmethod
    def sort(self):
        pass

    @abstractmethod
    def to_array(self):
        pass


    @abstractmethod
    def get_first(self):
        pass

    @abstractmethod
    def get_last(self):
        pass

    @abstractmethod
    def add_first(self, obj):
        pass

    @abstractmethod
    def add_last(self, obj):
        pass

    @abstractmethod
    def remove_first(self):
        pass

    @abstractmethod
    def remove_last(self):
        pass
