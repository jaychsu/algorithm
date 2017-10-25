import random
import re

class TinyUrl2:
    def __init__(self):
        self.char_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        self.host = 'http://tiny.url/'
        self.k = 6
        self.l2s = {}
        self.s2l = {}
        self.c_l2s = {}
        self.c_s2l = {}

    def saveUrl(self, hash, url, isCustom=False):
        if isCustom:
            self.c_l2s[url] = hash
            self.c_s2l[hash] = url
        else:
            self.l2s[url] = hash
            self.s2l[hash] = url

    def generateHash(self, k):
        res = ''
        j, n = 0, len(self.char_list)
        for i in range(k):
            j = random.randint(0, n - 1)
            res += self.char_list[j]
        return res

    """
    @param: long_url: a long url
    @param: key: a short key
    @return: a short url starts with http://tiny.url/
    """
    def createCustom(self, long_url, key):
        if not long_url or not key:
            return 'error'
        if long_url in self.c_l2s \
        and key in self.c_s2l:
            return self.host + self.c_l2s[long_url]
        if long_url not in self.c_l2s \
        and key not in self.c_s2l:
            self.saveUrl(key, long_url, isCustom=True)
            return self.host + self.c_l2s[long_url]
        return 'error'

    """
    @param: long_url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, long_url):
        if not long_url:
            return 'error'
        if long_url in self.l2s:
            return self.host + self.l2s[long_url]
        if long_url in self.c_l2s:
            return self.host + self.c_l2s[long_url]
        hash = self.generateHash(self.k)
        while hash in self.s2l:
            hash = self.generateHash(self.k)
        self.saveUrl(hash, long_url)
        return self.host + hash

    """
    @param: short_url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, short_url):
        if not short_url:
            return 'error'
        hash = re.match(self.host + '([a-zA-Z0-9]+)\/?', short_url)
        hash = hash.group(1) if hash else None
        if hash in self.s2l:
            return self.s2l[hash]
        if hash in self.c_s2l:
            return self.c_s2l[hash]
        return 'error'
