"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""

from collections import OrderedDict

class MiniCassandra:

    def __init__(self):
        self.storage = {}

    """
    @param: raw_key: a string
    @param: column_key: An integer
    @param: column_value: a string
    @return: nothing
    """
    def insert(self, raw_key, column_key, column_value):
        if raw_key not in self.storage:
            self.storage[raw_key] = OrderedDict()

        self.storage[raw_key][column_key] = column_value

    """
    @param: raw_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """
    def query(self, raw_key, column_start, column_end):
        if raw_key in self.storage:
            self.storage[raw_key] = OrderedDict(sorted(self.storage[raw_key].items()))
            return [
                Column(key, value)
                for key, value in self.storage[raw_key].items()
                if key >= column_start and key <= column_end
            ]
        else:
            return []

