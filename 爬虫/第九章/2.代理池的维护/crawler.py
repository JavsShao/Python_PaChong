import json
from pyquery import PyQuery

from .utils import get_page


class ProxyMetaclass(type):
    def __new__(cls, name, bases, attrs):
        count = 0
        attrs['__CrawlFunc__'] = []
        for k, v in attrs.items():
            if 'crawl_' in k:
                attrs['__CrawlFunc__'].append(k)
                count += 1
        attrs['__CrawlFuncCount__'] = count
        return type.__new__(cls, name, bases, attrs)

class Crawler(object, metaclass=ProxyMetaclass):

    def get_proxies(self, callback):
        proxies = []
        for proxy in eval('self.{}()'.format(callback)):
            print('成功获取到代理:', proxy)
            proxies.append(proxy)
        return proxies