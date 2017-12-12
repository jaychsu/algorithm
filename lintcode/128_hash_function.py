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

        hashcode = 0

        for char in key:
            hashcode = hashcode * MAGIC_NUMBER + ord(char)
            hashcode %= HASH_SIZE

        return hashcode
