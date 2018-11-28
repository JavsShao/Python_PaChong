import pymongo

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery


# 声明浏览器对象
browser = webdriver.Chrome()
wait = WebDriverWait(browser, 10)
# 要搜索的商品
KEYWORD = 'iPad'
MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = pymongo.MongoClient(MONGO_URL)
db = client[MONGO_DB]
MAX_PAGE = 100

def index_page(page):
    '''
    抓取索引页
    :param page: 页数
    :return:
    '''
    print('正在爬取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-pager div.form > input')))
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-pager div.form > span.btn.J_Submit')))
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-pager li.item.active > span'), str(page)))
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.m-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)


def get_products():
    '''
    提取商品数据
    :return:
    '''
    # 获取网页源码
    html = browser.page_source
    doc = PyQuery(html)
    items = doc('#mainsrp-itemlist .items .item').items()
    for item in items:
        product = {
            'image':item.find('.pic .img').attr('data-src'),
            'price':item.find('.price').text(),
            'deal':item.find('.deal-cnt').text(),
            # 这是标题，我自己修改的，不一定正确，权且试试看
            'title':item.find('.alt').text(),
            'shop':item.find('.shop').text(),
            'location':item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)

def save_to_mongo(result):
    '''
    保存至Mongodb
    :param result: 爬取的结果
    :return:
    '''
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到MongoDB成功！')
    except Exception as e:
        print('存储到MongoDB失败！失败原因是：',e)

def main():
    '''
    遍历每一页商品
    :return:
    '''
    for i in range(1, MAX_PAGE + 1):
        index_page(i)

if __name__ == '__main__':
    main()
