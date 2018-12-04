from .config import *
from requests import Request


class WeixinRequest(Request):

    def __init__(self, url, callback, method='GET', headers=None, need_proxy=False, fail_time=0, timeout=TIMEOUT):
        '''
        实现请求队列
        :param url: 请求地址
        :param callback:回调
        :param method:请求方式
        :param headers:请求头信息
        :param need_proxy:是否需要代理爬取
        :param fail_time:失败次数
        :param timeout:超时时间
        '''
        Request.__init__(self, method, url, headers)
        self.callback = callback
        self.need_proxy = need_proxy
        self.fail_time = fail_time
        self.timeout = timeout