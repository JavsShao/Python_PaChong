from requests import Session
from .db_redis import RedisQueue
from .requests import WeixinRequest
from urllib.parse import urlencode


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