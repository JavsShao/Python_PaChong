# 微博开头网址
from urllib.parse import urlencode

import requests

base_url = 'https://m.weibo.cn/api/container/getIndex?'

# 请求头信息
headers = {
    # 访问的主机地址
    'Host':'m.weibo.cn',
    # 重定向地址
    'Referer':'https://m.weibo.cn/u/3024395081',
    # 浏览器 & 操作系统信息
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    # Ajax请求
    'X-Requested-With': 'XMLHttpRequest',
}

# 获取请求的json结果
def get_page(page):
    # 请求的参数
    params = {
        'type':'uid',
        'value':'3024395081',
        'containerid':'1005053024395081',
        'page':page
    }
    # 访问的地址
    url = base_url + urlencode(params)
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError as e:
        print('错误！',e.args)

# 解析Json结果
def parse_page(json):
    if json:
        # cards在data参数下面
        items = json.get('data').get('cards')
        for item in items:
            item = item.get('mblog')
            weibo = {}
            weibo['id'] = item.get('id')
            weibo['text'] = item.get('text')
            weibo['attitudes'] = item.get('attitudes')
            weibo['comments'] = item.get('comment_count')
            weibo['reposts'] = item.get('reposts_count')
            yield weibo