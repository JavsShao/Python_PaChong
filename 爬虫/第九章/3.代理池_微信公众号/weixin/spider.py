from requests import Session
from weixin.config import *
from weixin.db_redis import RedisQueue
from weixin.mysql import MySQL
from urllib.parse import urlencode
import requests
from pyquery import PyQuery
from requests import ReadTimeout, ConnectionError

from weixin.requests import WeixinRequest


class Spider(object):
    base_url = 'http://weixin.sogou.com/weixin'
    keyword = '王小波'
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4,zh-TW;q=0.2,mt;q=0.2',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookies': 'ABTEST=0|1543895997|v1; SNUID=B47127661F1B6234529969041F45B847; IPLOC=CN1504; SUID=AB6F38791E24940A000000005C05FBBD; JSESSIONID=aaaoA-_JFCfJA7G5RA6Cw; SUV=00683D8E79386FAB5C05FBBEBBF24964; SUID=AB6F38797C20940A000000005C05FBBE; weixinIndexVisited=1; sct=1; ppinf=5|1543896110|1545105710|dHJ1c3Q6MToxfGNsaWVudGlkOjQ6MjAxN3x1bmlxbmFtZTo1OkhhbWRpfGNydDoxMDoxNTQzODk2MTEwfHJlZm5pY2s6NTpIYW1kaXx1c2VyaWQ6NDQ6bzl0Mmx1TGtRRlFmblFXNEF6ejBFbUdPVDB3WUB3ZWl4aW4uc29odS5jb218; pprdig=esSrGjNiB4a6X1q4W6Q6EOL9avsDaytXLxRgJbz4HU9kJOT9i7I4neWfohmMsljVpQNjmerh5HGwqMpF9cO6YF8E_Vy6Fkfm72vrkk-qEXXzwM3lXhNsitgQ6bhgIGivMjpVWjRM06Ab5ofzLWGYtG8Ep0Zr6dKn5sA0B0hVFcQ; sgid=08-33565741-AVwFicC5Z8r34ncHBNLIgC5k; ppmdig=1543896110000000e5b62a8b744f4e2b3b1a51b6a5c5231d',
        'Host': 'weixin.sogou.com',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
    }
    session = Session()
    queue = RedisQueue()
    mysql = MySQL()

    def get_proxy(self):
        '''
        从代理池获取代理
        :return:
        '''
        try:
            response = requests.get(PROXY_POOL_URL)
            if response.status_code == 200:
                print('获取到代理：', response.text)
                return response.text
            return None
        except requests.ConnectionError:
            return None

    def start(self):
        '''
        初始化工作
        :return:
        '''
        # 全局更新Headers
        self.session.headers.update(self.headers)
        start_url = self.base_url + '?' + urlencode({'query':self.keyword, 'type':2})
        weixin_request = WeixinRequest(url=start_url, callback=self.parse_index, need_proxy=True)
        # 调度第一个请求
        self.queue.add(weixin_request)

    def parse_index(self, response):
        '''
        解析索引页
        :param response: 响应
        :return: 新的响应
        '''
        doc = PyQuery(response.text)
        items = doc('.news-box .news-list li .txt-box h3 a').items()
        for item in items():
            url = item.attr('href')
            weixin_request = WeixinRequest(url=url, callback=self.parse_detail)
            yield weixin_request
        next = doc('#sogou_next').attr('href')
        if next:
            url = self.base_url + str(next)
            weixin_request = WeixinRequest(url=url, callback=self.parse_index, need_proxy=True)
            yield weixin_request

    def parse_detail(self, response):
        '''
        解析详情页
        :param response: 响应
        :return: 微信公众号文章
        '''
        doc = PyQuery(response.text)
        data = {
            'title':doc('.rich_media_title').text(),
            'content':doc('.rich_media_content').text(),
            'date':doc('#post-date').text(),
            'nickname':doc('#js_profile_qrcode > div > strong').text(),
            'wechat':doc('#js_profile_qrcode > div > p:nth-child(3) > span').text()
        }
        yield data

    def request(self, weixin_request):
        '''
        执行请求
        :param weixin_request: 请求
        :return: 响应
        '''
        try:
            if weixin_request.need_proxy:
                proxy = self.get_proxy()
                if proxy:
                    proxies = {
                        'http':'http://' + proxy,
                        'https':'https://' + proxy
                    }
                    return self.session.send(weixin_request.prepare(),timeout=weixin_request.timeout, allow_redirects=False, proxies=proxies)
            return self.session.send(weixin_request.prepare(), timeout=weixin_request.timeout, allow_redirects=False)
        except (ConnectionError, ReadTimeout) as e:
            print(e.args)
            return False

    def error(self, weixin_request):
        '''
        错误处理
        :param weixin_request: 请求
        :return:
        '''
        weixin_request.fail_time = weixin_request.fail_time + 1
        print('请求失败，',weixin_request.fail_time, '次数：', weixin_request.url)
        if weixin_request.fail_time < MAX_FAILED_TIME:
            self.queue.add(weixin_request)

    def schedule(self):
        """
        调度请求
        :return:
        """
        while not self.queue.empty():
            weixin_request = self.queue.pop()
            callback = weixin_request.callback
            print('调度：', weixin_request.url)
            response = self.request(weixin_request)
            if response and response.status_code in VALID_STATUSES:
                results = list(callback(response))
                if results:
                    for result in results:
                        print('新的请求：', type(result))
                        if isinstance(result, WeixinRequest):
                            self.queue.add(result)
                        if isinstance(result, dict):
                            self.mysql.insert('文章：', result)
                else:
                    self.error(weixin_request)
            else:
                self.error(weixin_request)

    def run(self):
        '''
        入口
        :return:
        '''
        self.start()
        self.schedule()

if __name__ == '__main__':
    spider = Spider()
    spider.run()

