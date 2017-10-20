import random
import re

class TinyUrl:
    def __init__(self):
        self.char_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.host = 'http://tiny.url/'
        self.k = 6
        self.l2s = {}
        self.s2l = {}

    def generateHash(self, k):
        res = ''
        j, n = 0, len(self.char_list)
        for i in range(k):
            j = random.randint(0, n - 1)
            res += self.char_list[j]
        return res

    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, url):
        if url in self.l2s:
            return self.host + self.l2s[url]
        hash = self.generateHash(self.k)
        while hash in self.s2l:
            hash = self.generateHash(self.k)
        self.l2s[url] = hash
        self.s2l[hash] = url
        return self.host + hash

    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, url):
        hash = re.match(self.host + '([A-Za-z0-9]+)\/?', url)
        hash = hash.group(1) if hash else None
        if hash in self.s2l:
            return self.s2l[hash]
