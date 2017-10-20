import random
import re

class TinyUrl:
    def __init__(self):
        self.char_list = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
        self.short_id_digit = 6
        self.host = 'http://tiny.url/'
        self.longurls = {}
        self.shortids = {}

    def generateShortId(self):
        result = ''
        for i in range(self.short_id_digit):
            index = random.randint(0, len(self.char_list) - 1)
            result += self.char_list[index]
        return result

    def toShortUrl(self, shortid):
        if isinstance(shortid, str):
            return self.host + shortid
        else:
            return None

    """
    @param: url: a long url
    @return: a short url starts with http://tiny.url/
    """
    def longToShort(self, url):
        if url in self.longurls:
            return self.toShortUrl(self.longurls[url])
        shortid = self.generateShortId()
        while shortid in self.shortids:
            shortid = self.generateShortId()
        self.longurls[url] = shortid
        self.shortids[shortid] = url
        return self.toShortUrl(shortid)

    """
    @param: url: a short url starts with http://tiny.url/
    @return: a long url
    """
    def shortToLong(self, url):
        shortid = re.match(self.host + '([A-Za-z0-9]+)\/?', url)
        shortid = shortid.group(1) if shortid else None
        if shortid in self.shortids:
            return self.shortids[shortid]
        return None
