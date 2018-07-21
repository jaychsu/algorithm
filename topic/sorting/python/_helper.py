from abc import ABC, abstractmethod
import collections


class SortBase(ABC):
    @classmethod
    @abstractmethod
    def sort(cls, iterable):
        """
        :type iterable: Iterable
        :rtype: list
        """
        pass

    @staticmethod
    def _is_valid_payload(iterable):
        """
        :type iterable: Iterable
        :rtype: bool
        """
        return isinstance(iterable, collections.Iterable)
