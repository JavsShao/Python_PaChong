import requests
import os

from urllib.parse import urlencode
from hashlib import md5


# 获取页面信息
def get_page(offset):
    # 请求的参数信息
    params = {
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':'20',
        'cur_tab':'1',
        'from':'search_tab',
        'pd':'synthesis'
    }
    url = 'https://www.toutiao.com/search_content/?' + urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except requests.ConnectionError:
        return None

# 解析页面
def get_images(json):
    if json.get('data'):
        for item in json.get('data'):
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield {
                    'image':'http:' + image.get('url'),
                    'title':title
                }

# 保存图片
def save_image(item):
    if not os.path.exists(item.get('title')):
        os.mkdir(item.get('title'))
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            if not os.path.exists(file_path):
                with open(file_path, "wb") as f:
                    f.write(response.content)
            else:
                print("下载完成！",file_path)
    except requests.ConnectionError:
        print('图片下载失败！')