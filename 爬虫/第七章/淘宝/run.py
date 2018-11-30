import time

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
        # get_url(url)
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

# def get_url():
#     #网址可以更改为用微博登录的网址'https://weibo.com/login.php?spm=a2107.1.0.0.337911d9Xjeo8U&entry=taobao&goto=https%3A%2F%2Flogin.taobao.com%2Faso%2Ftvs%3Fdomain%3Dweibo%26sid%3De14b81726a49329b0db026af4eff8357%26target%3D68747470733A2F2F7777772E7461'
#     url = 'https://login.taobao.com/member/login.jhtml?spm=a21bo.2017.754894437.1.5af911d9l2Cj72&f=top&redirectURL=https%3A%2F%2Fwww.taobao.com%2F'
#     #将网址更改微博登录网址可以省略这步直接用输入用户名密码阶段。
#     browser.get(url)
#     button_login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_QRCodeLogin > div.login-links > a.forget-pwd.J_Quick2Static')))
#     button_login.click()
#     time.sleep(2)
#     button_login1 = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#J_OtherLogin > a.weibo-login')))
#     button_login1.click()
#
#
#     EMAIL = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR,'#pl_login_logged > div > div:nth-child(2) > div > input')))
#
#     EMAIL.send_keys('微博用户名')
#     PASSWD = wait.until((EC.presence_of_element_located((By.CSS_SELECTOR,'#pl_login_logged > div > div:nth-child(3) > div > input'))))
#     PASSWD.send_keys('微博密码')
#     time.sleep(3)
#     button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#pl_login_logged > div > div:nth-child(7) > div:nth-child(1) > a > span')))
#     button.click()

if __name__ == '__main__':
    main()
