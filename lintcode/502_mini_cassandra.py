"""
Definition of Column:
class Column:
    def __init__(self, key, value):
        self.key = key
        self.value = value
"""


class MiniCassandra:

    storage = {}

    """
    @param: raw_key: a string
    @param: column_key: An integer
    @param: column_value: a string
    @return: nothing
    """
    def insert(self, raw_key, column_key, column_value):
        if raw_key not in self.storage:
            self.storage[raw_key] = {}

        self.storage[raw_key][column_key] = Column(column_key, column_value)

    """
    @param: raw_key: a string
    @param: column_start: An integer
    @param: column_end: An integer
    @return: a list of Columns
    """
    def query(self, raw_key, column_start, column_end):
        if raw_key not in self.storage:
            return []

        result = [
            column
            for column_key, column in self.storage[raw_key].items()
            if column_start <= column_key <= column_end
        ]

        return sorted(result, key=lambda column: column.key)
