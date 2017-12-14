class Solution:
    """
    @param: key: A string you should hash
    @param: HASH_SIZE: An integer
    @return: An integer
    """
    def hashCode(self, key, HASH_SIZE):
        if not key:
            return 0

        MAGIC_NUMBER = 33

        _code = 0
        for char in key:
            _code = (_code * MAGIC_NUMBER + ord(char)) % HASH_SIZE

        return _code
