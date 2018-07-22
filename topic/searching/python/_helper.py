from abc import ABC, abstractmethod


class SearchBase(ABC):
    @classmethod
    @abstractmethod
    def search(cls, iterable, val):
        """
        :type iterable: Iterable
        :type val: any
        :rtype: int
        """
        pass
