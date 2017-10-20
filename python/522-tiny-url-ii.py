import random
import re

class TinyUrl2:
    def __init__(self):
        self.host = 'http://tiny.url/'
        self.char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
        self.shortkey_digit = 6
        self.url2key = {}
        self.key2url = {}
        self.custom_url2key = {}
        self.custom_key2url = {}

    def formatShortUrl(self, key):
        return self.host + key

    def generateKey(self):
        key = ''
        index = 0
        for i in range(self.shortkey_digit):
            index = random.randint(0, len(self.char_list) - 1)
            key += self.char_list[index]
        return key

    """
    @param: long_url: a long url
    @param: key: a short key
    @return: a short url starts with http://tiny.url/
    """
    def createCustom(self, long_url, key):
        is_long_url_logged = long_url in self.custom_url2key
        is_custom_key_logged = key in self.custom_key2url
        if is_long_url_logged and is_custom_key_logged:
            return self.formatShortUrl(self.custom_url2key[long_url])
        if not is_long_url_logged and not is_custom_key_logged:
            self.custom_url2key[long_url] = key
            self.custom_key2url[key] = long_url
            return self.formatShortUrl(key)
        return 'error'

    """
    @param: long_url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, long_url):
        if long_url in self.url2key:
            return self.formatShortUrl(self.url2key[long_url])
        if long_url in self.custom_url2key:
            return self.formatShortUrl(self.custom_url2key[long_url])
        key = self.generateKey()
        while key in self.key2url:
            key = self.generateKey()
        self.url2key[long_url] = key
        self.key2url[key] = long_url
        return self.formatShortUrl(key)

    """
    @param: short_url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, short_url):
        key = re.match(self.host + '([A-Za-z0-9]+)\/?', short_url)
        key = key.group(1) if key else 'error'
        if key in self.key2url:
            return self.key2url[key]
        if key in self.custom_key2url:
            return self.custom_key2url[key]
        return 'error'
