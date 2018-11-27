import requests
import os

from urllib.parse import urlencode
from hashlib import md5
from multiprocessing.pool import Pool


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
    }
    base_url = 'https://www.toutiao.com/search_content/?'
    url = base_url + urlencode(params)
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
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield {
                    'image':'https:' + image.get('url'),
                    'title':title
                }

# 保存图片
def save_image(item):
    img_path = 'img' + os.path.sep + item.get('title')
    if not os.path.exists(img_path):
        # os.mkdir(item.get('title'))
        os.makedirs(img_path)
    try:
        response = requests.get(item.get('image'))
        if response.status_code == 200:
            # file_path = '{0}/{1}.{2}'.format(item.get('title'), md5(response.content).hexdigest(), 'jpg')
            file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                file_name=md5(response.content).hexdigest(),
                file_suffix='jpg')
            if not os.path.exists(file_path):
                with open(file_path, "wb") as f:
                    f.write(response.content)
                    print("成功下载图片！")
            else:
                print("已经下载了！",file_path)
    except requests.ConnectionError:
        print('图片下载失败！')

# 控制页数
def main(offset):
    json = get_page(offset)
    for item in get_images(json):
        print(item)
        save_image(item)

# 起始页数 和 终止页数
GROUP_START = 0
GROUP_END = 5

# 程序入口
if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_START, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()